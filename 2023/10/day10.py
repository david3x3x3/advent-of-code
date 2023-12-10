import sys

lines = open(sys.argv[1]).read().strip().split('\n')

grid = {}
grid2 = {}
# line drawing characters for better display
ch_to_line = {'F': '┌', 'L': '└', '7': '┐', 'J': '┘', '|': '│',
              '-': '─', '.': '▪', '@': '▓'}

for line_num, line in enumerate(lines):
    for ch_num, ch in enumerate(line):
        c = (line_num, ch_num)
        if ch == 'S':
            pos = c
        grid[c] = ch
grid_rows = line_num+1
grid_cols = ch_num+1

dird = {'F': {(-1, 0): (0, 1), (0, -1): (1, 0)},
        '7': {(0, 1): (1, 0), (-1, 0): (0, -1)},
        'J': {(1, 0): (0, -1), (0, 1): (-1, 0)},
        'L': {(0, -1): (-1, 0), (1, 0): (0, 1)},
        '|': {(1, 0): (1, 0), (-1, 0): (-1, 0)},
        '-': {(0, 1): (0, 1), (0, -1): (0, -1)}}

done = False

cw_dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
ccw_dirs = list(reversed(cw_dirs))

answer1 = 0
# figure out the starting direction
for next_dir in cw_dirs:
    dr, dc = next_dir
    pos2 = (pos[0]+dr, pos[1]+dc)
    if pos2 in grid and \
       grid[pos2] in dird and \
       next_dir in dird[grid[pos2]]:
        break
# follow the pipe
while True:
    # print(f'pos = {pos}')
    pos = (next_dir[0]+pos[0], next_dir[1]+pos[1])
    grid2[pos] = grid[pos]
    answer1 += 1
    if grid[pos] == 'S':
        break
    in_dir = (next_dir[0] * -1, next_dir[1] * -1)
    in_dirn = ccw_dirs.index(in_dir)
    next_dir = dird[grid[pos]][next_dir]
    while True:
        # mark the empty spaces to right of the pipe
        in_dirn = (in_dirn + 1) % 4
        if ccw_dirs[in_dirn] == next_dir:
            break
        pos2 = (pos[0]+ccw_dirs[in_dirn][0], pos[1]+ccw_dirs[in_dirn][1])
        if pos2 not in grid2:
            grid2[pos2] = '@'
# flood fill the marked inside regions
done = False
while not done:
    done = True
    for row in range(grid_rows):
        for col in range(grid_cols):
            if (row, col) in grid2 and grid2[(row, col)] == '@':
                for dr, dc in ccw_dirs:
                    row2 = row+dr
                    col2 = col+dc
                    if (row2, col2) not in grid2:
                        grid2[(row2, col2)] = '@'
                        done = False
# print the resulting grid and count the marked spaces
answer2 = 0
for row in range(grid_rows):
    for col in range(grid_cols):
        if (row, col) in grid2:
            ch = grid2[(row, col)]
        else:
            ch = '.'
        ch2 = ch_to_line[ch] if ch in ch_to_line else ch
        print(ch2, end='')
        if ch == '@':
            answer2 += 1
    print('')

answer1 //= 2

print(f'answer1 = {answer1}')
print(f'answer2 = {answer2}')
