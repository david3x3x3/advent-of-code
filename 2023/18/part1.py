import sys

lines = open(sys.argv[1]).read().strip().split('\n')

answer1 = 0

dirnames = 'XURDL'
dirs = ((0, 0), (-1, 0), (0, 1), (1, 0), (0, -1))

grid = {(0, 0): '#'}
pos = [0, 0]

minr = 0
minc = 0
maxr = 0
maxc = 0
for line in lines:
    dirname, dist, color = line.split()
    dist = int(dist)
    dr, dc = dirs[dirnames.find(dirname)]
    # print(dirname, dr, dc, dist)
    for i in range(dist):
        pos[0] += dr
        pos[1] += dc
        grid[tuple(pos)] = '#'
        # print(f'pos = {pos}')
        maxr = max(maxr, pos[0])
        minr = min(minr, pos[0])
        maxc = max(maxc, pos[1])
        minc = min(minc, pos[1])
        # print(minr, minc, maxr, maxc)

#done = False
done = True
grid[(-1, 0)] = '@'
#grid[(1, 1)] = '@'
while not done:
    done = True
    for row in range(minr, maxr+1):
        for col in range(minc, maxc+1):
            if (row, col) in grid and grid[(row, col)] == '@':
                for dr, dc in dirs:
                    row2 = row+dr
                    col2 = col+dc
                    if (row2, col2) not in grid:
                        grid[(row2, col2)] = '@'
                        done = False
for r1 in range(minr, maxr+1):
    print(f'{r1:3d}: ', end='')
    for c1 in range(minc, maxc+1):
        if (r1, c1) in grid:
            if (r1, c1) == (0, 0):
                ch = '@'
            else:
                ch = grid[(r1, c1)]
        else:
            ch = ' '
        print(ch, end='')
    print('')
print(minr, minc, maxr, maxc)
print(len(grid))
