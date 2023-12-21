import sys

lines = open(sys.argv[1]).read().strip().split('\n')
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
grid = {}
pos_list = set()

# load the map into a 5x5 array of duplicate maps
for line in lines:
    max_row = len(lines)
    max_col = len(lines[0])
    for mult_row in range(5):
        for mult_col in range(5):
            for line_num, line in enumerate(lines):
                for ch_num, ch in enumerate(line):
                    r2 = mult_row*max_row+line_num
                    c2 = mult_col*max_col+ch_num
                    if ch == 'S':
                        if mult_row == 2 and mult_col == 2:
                            pos_list.add((r2, c2))
                    grid[(r2, c2)] = ch
max_row2 = max_row * 5
max_col2 = max_row * 5

total_steps = 26501365
# total_steps = 2*131+65
cycles = total_steps//max_row
extra = total_steps % max_row

print('')
print(f'{total_steps} / {max_row} = {total_steps // max_row} rem {extra}')
print('')

# fill in the 5x5 array of maps
for steps in range(max_row*2+extra):
    # print(steps, len(pos_list))
    # print_grid(pos_list)
    pos_list2 = set()
    for pos in pos_list:
        for dr, dc, in dirs:
            pos2 = (pos[0]+dr, pos[1]+dc)
            if pos2 in grid and grid[pos2] != '#':
                pos_list2.add(pos2)
    pos_list = pos_list2
print(len(pos_list))

counts = [[0 for col in range(5)] for row in range(5)]
for r1 in range(max_row2):
    for c1 in range(max_col2):
        if (r1, c1) in pos_list:
            counts[r1//max_row][c1//max_col] += 1

# counts for each map in our array comes out like this:

#    0   932  5522   935     0
#  932  6415  7335  6427   935
# 5506  7335  7320  7335  5534
#  937  6411  7335  6427   931
#    0   937  5518   931     0

# we can multiply it as necessary when the map scales much larger

for row in counts:
    print(' '.join([f'{col:5}' for col in row]))
answer = 0
# 0, 0 is empty
answer += counts[0][1] * cycles
answer += counts[0][2]
answer += counts[0][3] * cycles
# 0, 4 is empty
# 1, 0 covered by 0, 1
answer += counts[1][1] * (cycles-1)
# I had to look up "center square numbers" for this:
answer += counts[1][2] * cycles**2
answer += counts[1][3] * (cycles-1)
# 1, 4 covered by 0, 3
answer += counts[2][0]
# 2, 1 covered by 1, 2
# center square number part 2:
answer += counts[2][2] * (cycles-1)**2
# 2, 3 covered by 1, 2
answer += counts[2][4]
answer += counts[3][0] * cycles
answer += counts[3][1] * (cycles-1)
# 3, 2 covered by 1, 2
answer += counts[3][3] * (cycles-1)
answer += counts[3][4] * cycles
# 4, 0 is empty
# 4, 1 covered by 3, 0
answer += counts[4][2]
# 4, 3 covered by 3, 4
# 4, 4 is empty
print(f'answer = {answer}')
# print(f'check = {len(pos_list)}')
