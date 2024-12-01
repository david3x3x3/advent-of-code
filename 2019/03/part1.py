import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    data = [line.strip().split(',') for line in fp.readlines()]

dirs = { "U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1) }

d = defaultdict(lambda: 0)
for pathnum, path in enumerate(data):
    r = 0
    c = 0
    for line in path:
        dr, dc = dirs[line[0]]
        steps = int(line[1:])
        # print(f"{pathnum} {dr} {dc} ({line[0]}) {steps}")
        for step in range(steps):
            r += dr
            c += dc
            d[(r, c)] |= (1 << pathnum)

if False:
    ks = list(d.keys())
    minr, minc = ks[0]
    maxr, maxc = ks[0]
    for k in ks:
        # minr = k[0] if k[0] < minr else minr
        minr = min(k[0], minr)
        maxr = max(k[0], maxr)
        minc = min(k[1], minc)
        maxc = max(k[1], maxc)
    print(k)
    print(minr, maxr)
    for r in range(minr, maxr+1):
        for c in range(minc, maxc+1):
            ch = '.' if (r, c) in d else ' '
            print(ch, end='')
        print('')

print(min([abs(k[0]) + abs(k[1]) for k in d if d[k] > 2]))
