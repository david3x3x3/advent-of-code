import sys


def make_groups(lines):
    groups = []
    prev = 0
    for line_num, line in enumerate(lines + ['']):
        if line == "":
            groups += [lines[prev:line_num]]
            prev = line_num + 1
    return groups


def check(g, num_rows, num_cols, omit=-1):
    for axis in (100, 1):
        if axis == 1:
            # flip grid diagonally
            g = {(c, r): g[(r, c)] for r, c in g}
            num_rows, num_cols = num_cols, num_rows
        for row in range(1, num_rows):
            found = True
            for col in range(num_cols):
                for row2 in range(num_rows-row):
                    if row-row2-1 >= 0 and \
                       g[(row+row2, col)] != g[(row-row2-1, col)]:
                        found = False
                        break
                if not found:
                    break
            if found and row*axis != omit:
                return row*axis
    return 0


if __name__ == '__main__':
    lines = open(sys.argv[1]).read().strip().split('\n')
    answer1 = 0
    answer2 = 0
    for group in make_groups(lines):
        score = 0
        grid = {}
        for line_num, line in enumerate(group):
            for ch_num, ch in enumerate(line):
                # store booleans rather than char to make it easier to flip
                grid[(line_num, ch_num)] = (ch == '#')
        num_rows = line_num + 1
        num_cols = ch_num + 1
        score1 = check(grid, num_rows, num_cols)
        answer1 += score1
        for row, col in grid:
            grid[(row, col)] = not grid[(row, col)]
            score2 = check(grid, num_rows, num_cols, score1)
            if score2 != 0:
                break
            grid[(row, col)] = not grid[(row, col)]
        answer2 += score2
    print(f'answer1 = {answer1}')
    print(f'answer2 = {answer2}')
