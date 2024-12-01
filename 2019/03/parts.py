import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    data = [line.strip().split(',') for line in fp.readlines()]

dirs = { "U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1) }

d = defaultdict(lambda: 0)
d2 = defaultdict(lambda: 0)
for pathnum, path in enumerate(data):
    r = 0
    c = 0
    dist = 0
    for line in path:
        dr, dc = dirs[line[0]]
        steps = int(line[1:])
        # print(f"{pathnum} {dr} {dc} ({line[0]}) {steps}")
        for step in range(steps):
            dist += 1
            r += dr
            c += dc
            d[(r, c)] |= (1 << pathnum)
            d2[(r, c)] += dist

if False:
    rs = [k[0] for k in d.keys()]
    cs = [k[1] for k in d.keys()]
    minr = min(rs)
    maxr = max(rs)
    minc = min(cs)
    maxc = max(cs)
    for r in range(minr, maxr+1):
        for c in range(minc, maxc+1):
            ch = d[(r,c)] if (r, c) in d else ' '
            print(ch, end='')
        print('')

print('Part 1:', min([abs(k[0]) + abs(k[1]) for k in d if d[k] > 2]))
print('Part 2:', min([d2[k] for k in d if d[k] > 2]))
