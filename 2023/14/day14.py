import sys


def tilt(lines, dir):
    moved = True
    while moved:
        moved = False
        for line_num in range(0, len(lines)):
            if line_num + dir[0] < 0 or \
               line_num + dir[0] == len(lines):
                continue
            for ch_num, ch in enumerate(lines[line_num]):
                if ch_num + dir[1] < 0 or \
                   ch_num + dir[1] == len(lines[0]):
                    continue
                if ch == 'O' and lines[line_num+dir[0]][ch_num+dir[1]] == '.':
                    lines[line_num+dir[0]][ch_num+dir[1]] = 'O'
                    lines[line_num][ch_num] = '.'
                    moved = True


def calc_load(lines):
    res = 0
    for line_num, line in enumerate(reversed(lines)):
        for ch in line:
            if ch == 'O':
                res += line_num+1
    return res


if __name__ == '__main__':
    lines = [list(it) for it in open(sys.argv[1]).read().strip().split('\n')]
    cycles = {}
    load_record = {}
    current = 0
    while True:
        tilt(lines, (-1, 0))
        if current == 0:
            print(f'answer1 = {calc_load(lines)}')
        tilt(lines, (0, -1))
        tilt(lines, (1, 0))
        tilt(lines, (0, 1))
        current += 1
        key = '/'.join([''.join(it) for it in lines])
        if key in cycles:
            first = cycles[key]
            print(f'repeated cycle {first} after cycle {current}')
            cycle_len = current-first
            print(f'cycle length = {cycle_len}')
            remain = 1000000000 - first
            remain %= cycle_len
            print(f'{remain} more cycles')
            print(f'looking up load after step {first+remain}')
            print(f'answer2 = {load_record[first+remain]}')
            break
        else:
            cycles[key] = current
            load_record[current] = calc_load(lines)
            # print(f'cycle {current} load = {load_record[current]}')
