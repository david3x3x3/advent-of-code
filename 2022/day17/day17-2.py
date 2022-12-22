#1000000000000
#1 000 000 000 000
#1 514 285 714 288

import sys, copy, hashlib

import hashlib

with open(sys.argv[1]) as fp:
    lines = [s.strip() for s in fp.readlines()]

pattern = lines[0]

with open('pieces.txt') as fp:
    lines = [s.strip() for s in fp.readlines()]

print(f'lines = {lines}')

pieces = []
lines2 = list(lines)

while True:
    if '' in lines2:
        blank = lines2.index('')
    else:
        pieces += [lines2]
        break
    pieces += [lines2[:blank]]
    del(lines2[:blank+1])

for i, piece in enumerate(pieces):
    print(f'\npiece {i}\n' + '\n'.join(piece))

piecenum = 0
jet = 0
height = 0
bigtarget = -1

mymap = []
while len(mymap) < height+3+len(pieces[piecenum]):
    mymap = [['.']*7] + mymap

x1 = 2
y1 = height + 2 + len(pieces[piecenum])

def drawmap(visible):
    mymap2 = copy.deepcopy(mymap)
    for y2, row in enumerate(piece):
        for x2, c in enumerate(row):
            if c == '#':
                mymap2[-(y1-y2+1)][x2+x1] = '@'
    text = [''.join(s) for s in mymap2[:50]]
    if visible:
        print('\n' + '\n'.join(text))
    else:
        return text


count = 0
rounds = 0
mytable = {}

piece = pieces[piecenum]
print('\n# start')
drawmap(True)
    
while True:
    #print('\n# jet')
    blocked=False
    if pattern[jet] == '<': # move left
        for y2 in range(len(piece)):
            x2 = 0
            while piece[y2][x2] == '.':
                x2 += 1
            if x1+x2 == 0 or mymap[-(y1-y2+1)][x1+x2-1] != '.':
                blocked = True
                break
        if not blocked:
            x1 -= 1
    elif pattern[jet] == '>': # move right
        for y2 in range(len(piece)):
            x2 = len(piece[y2])-1
            while piece[y2][x2] == '.':
                x2 -= 1
            if x1+x2 == 6 or mymap[-(y1-y2+1)][x1+x2+1] != '.':
                blocked = True
                break
        if not blocked:
            x1 += 1
    jet += 1
    if jet == len(pattern):
        jet = 0
        rounds += 1
        mypic = drawmap(False)
        myhash = hashlib.md5(''.join(mypic).encode('utf-8')).hexdigest()
        record = { 'height': height, 'count': count, 'rounds': rounds }
        print(f'# end of pattern {myhash}')
        if myhash in mytable:
            record1 = mytable[myhash]
            print(f'previous = {record1}')
            print(f'current  = {record}')
            pcs_per_rep = record['count']-record1['count']
            hgt_per_rep = record['height']-record1['height']
            rnds_per_rep = record['rounds']-record1['rounds']
            print(f'pcs_per_rep = {pcs_per_rep}')
            print(f'rnds_per_rep = {rnds_per_rep}')
            print(f'hgt_per_rep = {hgt_per_rep}')
            fake_reps = (1000000000000 - record['count']) // pcs_per_rep
            print(f'fake_reps = {fake_reps}')
            fake_height = fake_reps * hgt_per_rep
            print(f'fake_height = {fake_height}')
            bigtarget = 1000000000000 - fake_reps * pcs_per_rep
            print(f'bigtarget = {bigtarget}')
        mytable[myhash] = record
        # for k in mytable.keys():
        #     print(f'{k}: {mytable[k]}')
        
    #drawmap(True)
    #print('\n# fall')
    # check if resting
    blocked = False
    for x2 in range(len(piece[0])):
        y2 = len(piece)-1
        while piece[y2][x2] == '.':
            y2 -= 1
        if y1-y2 == 0 or mymap[-(y1-y2)][x1+x2] != '.':
            blocked = True
            break
    #print(f'check if resting, y1={y1}, height={height}')
    #if y1-len(piece)+1 == height:
    if blocked:
        # draw the piece on the map
        for y2, row in enumerate(pieces[piecenum]):
            for x2, c in enumerate(row):
                if c == '#':
                    mymap[-(y1-y2+1)][x2+x1] = c
        #height += len(piece)
        height = max(height,y1+1)
        piecenum += 1
        if piecenum == len(pieces):
            piecenum = 0
        piece = pieces[piecenum]
        while len(mymap) < height+3+len(piece):
            mymap = [['.']*7] + mymap
        y1 = height + 2 + len(piece)
        x1 = 2
        #print('\n# new piece')
        #drawmap(True)
        count += 1
        if count == bigtarget:
            print(f'height = {height+fake_height}')
            exit(0)
        continue
    y1 -= 1
    #drawmap(True)
