import sys, re
from collections import namedtuple

Pair = namedtuple('Pair', ['dist', 'x1', 'y1', 'x2', 'y2'])

data = []
with open(sys.argv[1]) as fp:
    for words in [x.strip().split() for x in fp.readlines()]:
        n = []
        for i in ((2,'x1'),(3,'y1'),(8,'x2'),(9,'y2')):
            n += [int(words[i[0]].split('=')[1].strip(':,'))]
        data += [Pair(dist=abs(n[0]-n[2])+abs(n[1]-n[3]), x1=n[0], y1=n[1], x2=n[2], y2=n[3])]

targety = int(sys.argv[2])
starty = int(sys.argv[3])
endy = int(sys.argv[4])

print('PART 1')

segs = []
beacons = set()

for i, d in enumerate(data):
    if d.y1-d.dist <= targety and d.y1+d.dist >= targety:
        dist2 = d.dist-abs(d.y1-targety)
        segs += [[d.x1-dist2, d.x1+dist2]]
        if d.y2 == targety:
            beacons.add(d.x2)

print('\n'.join(map(str,segs)))
print(f'beacons = {list(beacons)}')
min2 = segs[0][0]
max2 = segs[0][1]
for seg in segs[1:]:
    if seg[0] < min2:
        min2 = seg[0]
    if seg[1] > max2:
        max2 = seg[1]
print(max2-min2+1-len(beacons))

print('PART 2')

print(f'checking {len(data)} sensors')

for targety in range(starty, endy+1):
    if targety % 1000000 == 0:
        print(f' checking y = {targety}')
    rowsegs = [[starty, endy]]
    for i, d in enumerate(data):
        if d.y1-d.dist <= targety and d.y1+d.dist >= targety:
            dist2 = d.dist-abs(d.y1-targety)
            # left and right end of segment to check
            seg2 = [d.x1-dist2, d.x1+dist2]
            # erase all parts of rowsegs covered by seg2
            #print(f'  seg2 = {seg2}', flush=True)
            temprow = []
            for i in range(len(rowsegs)):
                rowseg = list(rowsegs[i])
                #print(f'   rowseg = {rowseg}', flush=True)
                if seg2[0] < rowseg[0]:
                    # seg2 starts before rowseg
                    if seg2[1] < rowseg[0]:
                        #print('    # missed to the left')
                        temprow += [rowseg]
                    elif seg2[1] < rowseg[1]:
                        #print('    #covered left part 1')
                        rowseg[0] = seg2[1]+1
                        temprow += [rowseg]
                    #else:
                        # else covered entirely; don't keep
                        #print('    #covered entirely 2')
                elif seg2[0] == rowseg[0]:
                    # seg2 starts at left end of rowseg
                    if seg2[1] < rowseg[1]:
                        #print('    #covered left part 2')
                        rowseg[0] = seg2[1]+1
                        temprow += [rowseg]
                    #else:
                        # else covered entirely; don't keep
                        #print('    #covered entirely 2')
                elif seg2[0] <= rowseg[1]:
                    # seg2 starts within rowseg
                    if seg2[1] < rowseg[1]:
                        #print('    # seg2 splits rowseg in two')
                        temprow += [[rowseg[0], seg2[0]-1]]
                        rowseg[0] = seg2[1]+1
                        temprow += [rowseg]
                    else:
                        #print('    # seg2 covers right part of rowseg')
                        rowseg[1] = seg2[0]-1
                        temprow += [rowseg]
                else:
                    #print('    # seg2 missed rowseg to the right')
                    temprow += [rowseg]
                #print(f'    temprow = {temprow}')
            rowsegs = temprow
    if len(rowsegs):
        break
print(f'y = {targety}')
print(f' rowsegs = {rowsegs}')
print(f'freq = {4000000*rowsegs[0][0]+targety}')
