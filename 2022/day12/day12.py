import sys

with open(sys.argv[1]) as fp:
    map = [x.strip() for x in fp.readlines()]

#print(map)
#print('\n'.join(map))

dists = [[-1]*len(r) for r in map]

for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c] == 'E':
            dists[r][c] = 0

#print('\n'.join([' '.join(['%2d' % y for y in x]) for x in dists]))

def get_height(r, c):
    letter = map[r][c]
    if letter == 'E':
        return 26
    elif letter == 'S':
        return 1
    else:
        return ord(letter)-ord('a')+1

depth = 0
changed = True
while changed:
    changed = False
    for r1 in range(len(dists)):
        for c1 in range(len(dists[r1])):
            if dists[r1][c1] != depth:
                continue
            height = get_height(r1,c1)
            for dir in ((0,1),(1,0),(0,-1),(-1,0)):
                r2 = r1 + dir[0]
                c2 = c1 + dir[1]
                if r2 >= 0 and r2 < len(map) and c2 >= 0 and c2 < len(map[0]) and \
                   dists[r2][c2] < 0 and height - get_height(r2, c2) < 2:
                    changed = True
                    dists[r2][c2] = depth + 1
                    #print('')
                    #print('\n'.join([' '.join(['%2d' % y for y in x]) for x in dists]))
    depth += 1

#print('\n'.join([' '.join(['%3d' % y for y in x]) for x in dists]))

print('part 1:')
for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c] == 'S':
            print(dists[r][c])

print('')
print('part 2:')
shortest = 10000
for r in range(len(map)):
    for c in range(len(map[r])):
        if (map[r][c] == 'S' or map[r][c] == 'a') and dists[r][c] > 0 and dists[r][c] < shortest:
            shortest = dists[r][c]
print(shortest)
