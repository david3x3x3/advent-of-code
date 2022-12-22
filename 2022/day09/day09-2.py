import sys

knots = []
for i in range(10):
    knots += [[0,0]]
    
path = set()
path.add(tuple(knots[9]))
with open(sys.argv[1]) as fp:
    for line in [x.strip().split(' ') for x in fp.readlines()]:
        print(line)
        dir = ((0,1),(1,0),(0,-1),(-1,0))['RDLU'.find(line[0])]
        for n in range(int(line[1])):
            knots[0][0] += dir[0]
            knots[0][1] += dir[1]
            for k in range(9):
                dr = knots[k][0]-knots[k+1][0]
                dc = knots[k][1]-knots[k+1][1]
                if abs(dr) > 1 or abs(dc) > 1:
                    if dr == -2:
                        dr = -1
                    if dr == 2:
                        dr = 1
                    if dc == -2:
                        dc = -1
                    if dc == 2:
                        dc = 1
                    knots[k+1][0] += dr
                    knots[k+1][1] += dc
            print(knots)
            path.add(tuple(knots[9]))
print(len(path))
