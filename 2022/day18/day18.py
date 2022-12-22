import sys

with open(sys.argv[1]) as fp:
    cubes = [list(map(int,s.strip().split(','))) for s in fp.readlines()]
    
#print(cubes)
cs = set()
flooded = set()
for cube in cubes:
    cs.add(tuple(cube))

score = len(cubes)*6

mins = [cubes[0][0],cubes[0][1],cubes[0][2]]
maxs = [cubes[0][0],cubes[0][1],cubes[0][2]]

for cube in cubes:
    for axis in range(3):
        for dir in [-1,1]:
            cube[axis] += dir
            if tuple(cube) in cs:
                score -= 1
            cube[axis] += dir
            if cube[axis] <= mins[axis]:
                mins[axis] = cube[axis]-1
            if cube[axis] >= maxs[axis]:
                maxs[axis] = cube[axis]+1
print(score)
print(f'mins = {mins}')
print(f'maxs = {maxs}')

checklist = [list(mins)]
flooded.add(tuple(mins))

while len(checklist):
    #print(checklist)
    tmpcheck = []
    for check in checklist:
        for axis in range(3):
            for dir in [-1,1]:
                check[axis] += dir
                if check[0] >= mins[0] and check[0] <= maxs[0] and \
                   check[1] >= mins[1] and check[1] <= maxs[1] and \
                   check[2] >= mins[2] and check[2] <= maxs[2] and \
                   tuple(check) not in flooded and \
                   tuple(check) not in cs:
                    tmpcheck += [list(check)]
                    flooded.add(tuple(check))
                check[axis] -= dir
    checklist = tmpcheck

print(f'len flooded = {len(flooded)}')

for x in range(mins[0], maxs[0]+1):
    for y in range(mins[1], maxs[1]+1):
        for z in range(mins[2], maxs[2]+1):
            if (x,y,z) not in cs and (x,y,z) not in flooded:
                #print(f'{x},{y},{z} is not flooded')
                cube = [x,y,z]
                for axis in range(3):
                    cube[axis] -= 1
                    if tuple(cube) in cs:
                        score -= 1
                    cube[axis] += 2
                    if tuple(cube) in cs:
                        score -= 1
                    cube[axis] -= 1
                    if cube[axis] <= mins[axis]:
                        mins[axis] = cube[axis]-1
                    if cube[axis] >= maxs[axis]:
                        maxs[axis] = cube[axis]+1
print(score)
