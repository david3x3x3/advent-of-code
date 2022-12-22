import sys

with open(sys.argv[1]) as fp:
    lines = [x.strip() for x in fp.readlines()]

best = 0
for r1 in range(len(lines)):
    for c1 in range(len(lines[r1])):
        score = 1
        for dir in ((0,1),(0,-1),(1,0),(-1,0)):
            visible = 0
            pos = [r1+dir[0],c1+dir[1]]
            while pos[0] >= 0 and pos[0] < len(lines) and \
                  pos[1] >= 0 and pos[1] < len(lines[0]):
                visible += 1
                if int(lines[pos[0]][pos[1]]) >= int(lines[r1][c1]):
                    break
                pos[0] += dir[0]
                pos[1] += dir[1]
            score *= visible
        if score > best:
            best = score
print(best)
