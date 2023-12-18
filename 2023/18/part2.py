import sys

lines = open(sys.argv[1]).read().strip().split('\n')

answer1 = 0

dirnames = 'RDLU'
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
pos = [0, 0]
rows = {(0, 0): [[0, 0]]}

hlines = []
vlines = []
hset = set()

for line in lines:
    dirname, dist, color = line.split()
    if False:
        dist = int(dist)
        dr, dc = dirs[dirnames.find(dirname)]
    else:
        dist = int(color[2:-2], 16)
        dir = dirnames[int(color[-2])]
        dirname = dirnames[int(color[-2])]
    # print(dist, dir, color, flush=True)
    # print(dirname, dr, dc, dist)
    if dirname == 'R':
        hlines += [{'row': pos[0], 'range': [pos[1], pos[1]+dist]}]
        hset.add(pos[0])
        pos[1] += dist
    if dirname == 'L':
        hlines += [{'row': pos[0], 'range': [pos[1]-dist, pos[1]]}]
        hset.add(pos[0])
        pos[1] -= dist
    if dirname == 'D':
        vlines += [{'col': pos[1], 'range': [pos[0], pos[0]+dist]}]
        pos[0] += dist
    if dirname == 'U':
        vlines += [{'col': pos[1], 'range': [pos[0]-dist, pos[0]]}]
        pos[0] -= dist
    
print(f'hlines = {hlines}')
print(f'vlines = {vlines}')
hset = sorted(list(hset))
print(f'hset = {hset}')
answer = 0
# find area between hline rows
for rpos, r1 in enumerate(hset[:-1]):
    if r1+1 == hset[rpos+1]:
        # no space between hlines
        continue
    r2 = r1 + 1
    print(f'scanning row {r2}: ', end='')
    vset = []
    for line in vlines:
        if r2 >= line['range'][0] and r2 <= line['range'][1]:
            vset += [line['col']]
    vset = sorted(vset)
    hcover = 0
    print(f'found {vset}')
    for i in range(0, len(vset), 2):
        c1, c2 = vset[i], vset[i+1]
        hcover += c2-c1+1
    #print(f'hcover = {hcover}')
    hcover2 = hcover * (hset[rpos+1]-r2)
    answer += hcover2
    #print(f'hcover2 = {hcover2}')
# find area OF hline rows
# for rpos, r1 in enumerate(hset[:-1]):
print(f'answer = {answer}')
# print('AREA OF ROWS')
for r1 in hset:
    segs = []
    # print(f'scanning row {r1}: ', end='')
    for hline in hlines:
        if hline['row'] == r1:
            c1, c2 = hline['range']
            check1 = (r1, c1) in [(vl['range'][0], vl['col']) for vl in vlines]
            check2 = (r1, c2) in [(vl['range'][0], vl['col']) for vl in vlines]
            is_even = (check1 == check2)
            segs += [(c1, c2, is_even)]
    # print(f'segs = {segs}')
    for vline in vlines:
        if not (r1 >= vline['range'][0] and r1 <= vline['range'][1]):
            continue
        c3 = vline['col']
        do_count = True
        for seg in segs:
            if c3 >= seg[0] and c3 <= seg[1]:
                do_count = False
                break
        if do_count:
            segs += [(c3, c3, False)]
    segs = sorted(segs)
    print(f'combined segs = {segs}')
    hcover = 0
    pen_down = False
    hpos = segs[0][0]
    while len(segs):
        hcover += segs[0][1]-segs[0][0]+1
        hpos = segs[0][1]+1
        if not segs[0][2]: # even
            pen_down = not pen_down
        if pen_down:
            hcover += segs[1][0]-hpos
        segs.pop(0)
    print(f'hcover = {hcover}')
    answer += hcover

print(f'answer = {answer}')
