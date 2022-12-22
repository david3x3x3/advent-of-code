import sys

with open(sys.argv[1]) as fp:
    lines = [x.strip() for x in fp.readlines()]

scans = []
for c in range(len(lines[0])):
    scans += [([0,c],(1,0))]
    scans += [([len(lines)-1,c],(-1,0))]
for r in range(len(lines)):
    scans += [([r,0],(0,1))]
    scans += [([r,len(lines[0])-1],(0,-1))]

visible = set()
for pos, dir in scans:
    top = -1
    while pos[0] >= 0 and pos[0] < len(lines) and \
          pos[1] >= 0 and pos[1] < len(lines[0]):
        x = int(lines[pos[0]][pos[1]])
        if x > top:
            visible.add(tuple(pos))
            top = x
        pos[0] += dir[0]
        pos[1] += dir[1]
print(len(visible))
