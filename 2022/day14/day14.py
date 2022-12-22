import sys

with open(sys.argv[1]) as fp:
    #lines = [x.strip() forfp.readlines().split() if i % 2 == 1]
    walls =[[list(map(int,y.split(',')))
        for y in [x for i, x in enumerate(line.strip().split()) if i%2 == 0]]
            for line in fp.readlines()]

for part in range(1,3):
    print(f'Part {part}\n')
    maxr = minr = 0
    maxc = minc = 500

    #print('\n'.join(map(str,walls)))
    for wall in walls:
        for coord in wall:
            if coord[0] > maxc:
                maxc = coord[0]
            if coord[0] < minc:
                minc = coord[0]
            if coord[1] > maxr:
                maxr = coord[1]
            if coord[1] < minr:
                minr = coord[1]
    minc -= 1
    maxc += 1
    width = maxc-minc+1
    height = maxr-minr+1
    #print(f'width = {width}')
    #print(f'height = {height}')
    mymap = [['.']*width for r in range(height)]
    for wall in walls:
        curs = list(wall[0])
        mymap[curs[1]][curs[0]-minc] = '#'
        for coord in wall[1:]:
            while curs != coord:
                if curs[0] < coord[0]:
                    curs[0] += 1
                elif curs[0] > coord[0]:
                    curs[0] -= 1
                if curs[1] < coord[1]:
                    curs[1] += 1
                elif curs[1] > coord[1]:
                    curs[1] -= 1
                mymap[curs[1]][curs[0]-minc] = '#'

    if part == 2:
        # add an infinite floor for part 2
        mymap += [['.']*width]
        mymap += [['#']*width]
        height += 2
        maxr += 2

    # print the empty map
    #print('\n'.join([''.join(row) for row in mymap]) + '\n', flush=True)

    score = 0
    full = False
    startcol = 500-minc
    while not full:
        falling = True
        curs = [startcol,0]
        while falling:
            if mymap[curs[1]][curs[0]] == 'o':
                # starting point is blocked
                falling = False
                full = True
                break
            ok = False
            for dir in ((0,1),(-1,1),(1,1)):
                target = [curs[0]+dir[0],curs[1]+dir[1]]
                if mymap[target[1]][target[0]] == '.':
                    ok = True
                    break
            if ok:
                curs = list(target)
                if curs[1] == maxr:
                    falling = False
                    full = True
                    break
                if curs[0] == 0:
                    mymap = [['.'] + r for r in mymap]
                    mymap[-1][0] = '#'
                    curs[0] += 1
                    startcol += 1
                elif curs[0]+1 == len(mymap[0]):
                    mymap = [r + ['.'] for r in mymap]
                    mymap[-1][-1] = '#'
            else:
                falling = False
                mymap[curs[1]][curs[0]] = 'o'
                score += 1
                #print('\n'.join([''.join(row) for row in mymap]) + '\n', flush=True)
                break

    print('\n'.join([''.join(row) for row in mymap]) + '\n', flush=True)
    print(f'Score = {score}\n')
