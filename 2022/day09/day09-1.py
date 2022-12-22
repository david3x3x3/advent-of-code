import sys

h = [0,0]
t = [0,0]

path = set()
path.add(tuple(t))
with open(sys.argv[1]) as fp:
    for line in [x.strip().split(' ') for x in fp.readlines()]:
        print(line)
        dir = ((0,1),(1,0),(0,-1),(-1,0))['RDLU'.find(line[0])]
        for n in range(int(line[1])):
            h[0] += dir[0]
            h[1] += dir[1]
            dr = h[0]-t[0]
            dc = h[1]-t[1]
            if abs(dr) > 1 or abs(dc) > 1:
                print('moving tail')
                if dr == -2:
                    dr = -1
                if dr == 2:
                    dr = 1
                if dc == -2:
                    dc = -1
                if dc == 2:
                    dc = 1
                t[0] += dr
                t[1] += dc
            path.add(tuple(t))
            print(h, t)
print(len(path))
