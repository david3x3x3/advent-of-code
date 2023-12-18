import sys, copy
from collections import defaultdict

dirnames = 'XURDL'
# printing upside down for debugging
# dirnames = 'XDRUL'
dirs = ((0, 0), (-1, 0), (0, 1), (1, 0), (0, -1))
lines = open(sys.argv[1]).read().strip().split('\n')
grid = {}
dists = defaultdict(dict)
for linenum, line in enumerate(lines):
    # print(f'line = {line}')
    for chnum, ch in enumerate(line):
        # print(linenum, chnum, ch)
        grid[(linenum, chnum)] = int(ch)
numrows = linenum + 1
numcols = chnum + 1
dists[(numrows-1, numcols-1)][((0, 0), 0)] = 0
steps = 0
done = False
while not done:
    done = True
    # if False:
    if steps % 10 == 0:
        print(f'step {steps}')
    if False:
        # for r1 in range(numrows-1, -1, -1):
        for r1 in range(numrows):
            for c1 in range(numcols):
                print(f'{r1:02d},{c1:02d} ', end='')
            print('')
            for c1 in range(numcols):
                print(f'{str(grid[(r1, c1)]):6s}', end='')
            print('')
            for n in range(12):
                for c1 in range(numcols):
                    disp = '     '
                    if (r1, c1) in dists and len(dists[(r1, c1)]) > n:
                        k2, v2 = list(dists[(r1, c1)].items())[n]
                        disp = str(k2[1]) + dirnames[dirs.index(k2[0])] + '%03d' % v2
                    print(disp, end=' ')
                print('')
            print('')
        # print('\n'.join(list(map(str, dists.items()))))
    steps += 1
    dists2 = copy.deepcopy(dists)
    # dists2 = dists
    for r1 in range(numrows):
        for c1 in range(numcols):
            if (r1, c1) not in dists:
                continue
            d = dists[(r1, c1)]
            for prev, l1 in d:
                dv1 = d[(prev, l1)]
                dv2 = dv1 + grid[(r1, c1)]
                for dr, dc in dirs[1:]:
                    if (dr*-1, dc*-1) == prev:
                        continue
                    r2 = r1 + dr
                    c2 = c1 + dc
                    if r2 < 0 or r2 >= numrows or c2 < 0 or c2 >= numcols or \
                       (r2, c2) == (numrows-1, numcols-1):
                        continue
                    d2 = dists2[(r2, c2)]
                    if (dr, dc) == prev:
                        l2 = l1 + 1
                    else:
                        l2 = 1
                    if prev != (0, 0) and (dr, dc) != prev and l1 < 4:
                        continue
                    if l2 > 10:
                        continue
                    if ((dr, dc), l2) in d2 and d2[((dr, dc), l2)] <= dv2:
                        continue
                    d2[((dr, dc), l2)] = dv2
                    done = False
    dists = dists2
print(min(dists[(0, 0)].values()))
