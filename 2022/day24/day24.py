import sys
import copy
from collections import defaultdict

with open(sys.argv[1]) as fp:
    m = [list(s.strip()) for s in fp.readlines()]

dirs = ((0,1),(1,0),(0,-1),(-1,0))
dirsf = ((0,1),(1,0),(0,-1),(-1,0),(0,0))
dirsym = '>v<^'
bliz = set()

def mapfill(with_elves):
    global empty
    global bliz
    m2 = copy.deepcopy(empty)
    stacks = defaultdict(lambda: 0)
    for (r1,c1),dir in bliz:
        stacks[(r1,c1)] += 1
    for (r1,c1),dir in bliz:
        ch = dirsym[dir]
        if stacks[(r1,c1)] > 1:
            ch = f'{stacks[(r1,c1)]}'
        m2[r1][c1] = ch
    if with_elves:
        for r1,c1 in elves:
            m2[r1][c1] = 'E'
    return m2

def printmap():
    m2 = mapfill(True)
    print('\n'.join([''.join(r) for r in m2]) + '\n')

def advanceb(b):
    b2 = set()
    for (r1,c1),dir in b:
        #print(r1, c1, dir)
        r2 = r1 + dirs[dir][0]
        c2 = c1 + dirs[dir][1]
        if r2 < 1:
            r2 = len(m)-2
        elif r2 > len(m)-2:
            r2 = 1
        elif c2 < 1:
            c2 = len(m[0])-2
        elif c2 > len(m[0])-2:
            c2 = 1
        b2.add(((r2,c2),dir))
    return b2

def advancee(es1):
    es2 = set()
    m2 = mapfill(False)
    for e in es1:
        for dir in dirsf:
            r2 = e[0]+dir[0]
            c2 = e[1]+dir[1]
            if r2 >= 0 and c2 >= 0 and r2 < len(m2) and m2[r2][c2] == '.':
                es2.add((r2,c2))
    return es2

empty = copy.deepcopy(m)
for r1, row in enumerate(m):
    for c1, sym in enumerate(row):
        if sym in dirsym:
            dir = dirsym.index(sym)
            bliz.add(((r1,c1),dir))
            empty[r1][c1] = '.'
            
elves = set()
elves.add((0,1))

step = 0
stage = 1
while(True):
    #print(f'- step {step}')
    #printmap()
    if stage == 1 and (len(m)-1,len(m[0])-2) in elves:
        stage = 2
        elves = set()
        elves.add((len(m)-1,len(m[0])-2))
        print(f'part 1 = {step}')
    elif stage == 2 and (0,1) in elves:
        stage = 3
        elves = set()
        elves.add((0,1))
    if stage == 3 and (len(m)-1,len(m[0])-2) in elves:
        print(f'part 2 = {step}')
        exit(0)
    bliz = advanceb(bliz)
    elves = advancee(elves)
    step += 1
