import sys

lines = open(sys.argv[1]).read().strip().split('\n')

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

answer1 = 0

grid = {}
pos_list = set()
for line in lines:
    print(f'line = |{line}|')
    for line_num, line in enumerate(lines):
        for ch_num, ch in enumerate(line):
            if ch == 'S':
                pos_list.add((line_num, ch_num))
                ch = '.'
            grid[(line_num, ch_num)] = ch
    max_row = line_num + 1
    max_col = ch_num + 1


def print_grid(pl):
    for r1 in range(max_row):
        for c1 in range(max_col):
            if (r1, c1) in pl:
                ch = 'O'
            else:
                ch = grid[(r1, c1)]
            print(ch, end='')
        print('')
    print('')


for steps in range(64):
    # print_grid(pos_list)
    pos_list2 = set()
    for pos in pos_list:
        for dr, dc, in dirs:
            pos2 = (pos[0]+dr, pos[1]+dc)
            if pos2 in grid and grid[pos2] != '#':
                pos_list2.add(pos2)
    pos_list = pos_list2
print_grid(pos_list)
print(len(pos_list))
