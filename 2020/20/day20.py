import sys
import math
from collections import defaultdict


def make_groups(lines):
    groups = []
    prev = 0
    for line_num, line in enumerate(lines + ['']):
        if line == "":
            groups += [lines[prev:line_num]]
            prev = line_num + 1
    return groups


def rotate(p):
    p2 = []
    for col_num in range(len(p)):
        r2 = ''
        for row_num in range(len(p)-1, -1, -1):
            r2 += p[row_num][col_num]
        p2 += [r2]
    for r in range(len(p)):
        p[r] = p2[r]


def flip(p):
    for r in range(len(p)):
        p[r] = ''.join(reversed(p[r]))


def printpuz(placed):
    while len(placed) < width * width:
        placed = placed + [(0, 0)]
    for r1 in range(width):
        for c1 in range(width):
            p = placed[r1*width+c1]
            print(f'+-{p[0]}/{p[1]}---', end='')
        print('+')
        for r2 in range(piecesize):
            print('', end='|')
            for c1 in range(width):
                p = placed[r1*width+c1]
                print(pieces[p[0]][p[1]][r2], end='|')
            print('')
    print(('+' + '-'*piecesize) * width + '+')


def find_monster(placed):
    sol = []
    for r1 in range(width):
        for r2 in range(1, piecesize-1):
            sol0 = ''
            for c1 in range(width):
                p = placed[r1*width+c1]
                sol0 += pieces[p[0]][p[1]][r2][1:-1]
            sol += [sol0]
    mon_locs = []
    pat = ('                  # ',
           '#    ##    ##    ###',
           ' #  #  #  #  #  #   ')
    for r1, s in enumerate(pat):
        for c1, ch in enumerate(s):
            if ch == '#':
                mon_locs += [(r1, c1)]
    mon_rows, mon_cols = r1+1, c1+1
    for flips in range(2):
        for rot in range(4):
            scratch = [list(it) for it in sol]
            found2 = False
            for r1 in range(len(sol)-mon_rows+1):
                for c1 in range(len(sol[0])-mon_cols+1):
                    found = True
                    for r2, c2 in mon_locs:
                        if sol[r1+r2][c1+c2] != '#':
                            found = False
                            break
                    if found:
                        found2 = True
                        for r2, c2 in mon_locs:
                            scratch[r1+r2][c1+c2] = 'O'
            scratch = [''.join(it) for it in scratch]
            if found2:
                print('\n' + '\n'.join(scratch))
                dd = defaultdict(lambda: 0)
                for ch in ''.join(scratch):
                    dd[ch] += 1
                res = dd['#']
            rotate(sol)
        flip(sol)
    return res


def search(placed, remain):
    global pieces, width
    if len(remain) == 0:
        printpuz(placed)
        answer1 = 1
        for r1 in (0, width-1):
            for c1 in (0, width-1):
                answer1 *= placed[r1*width+c1][0]
        print(f'answer1 = {answer1}')
        answer2 = find_monster(placed)
        print(f'answer2 = {answer2}')
        return 1
    for i, piecenum in enumerate(remain):
        remain2 = list(remain)
        del remain2[i]
        for rot, piece in enumerate(pieces[piecenum]):
            matched = True
            if len(placed) % width != 0:
                prev_num, prev_rot = placed[-1]
                for rnum, r in enumerate(piece):
                    if pieces[prev_num][prev_rot][rnum][-1] != r[0]:
                        matched = False
                        break
            if matched and len(placed) > width:
                prev_num, prev_rot = placed[-width]
                for cnum, c in enumerate(piece[0]):
                    if pieces[prev_num][prev_rot][-1][cnum] != c:
                        matched = False
                        break
            if matched:
                res = search(placed + [(piecenum, rot)], remain2)
                if res != 0:
                    return res
    return 0


if __name__ == '__main__':
    lines = open(sys.argv[1]).read().strip().split('\n')
    groups = make_groups(lines)
    width = int(math.sqrt(len(groups)))
    remain = []
    piecesize = len(groups[0][1])
    dummy = [' ' * piecesize] * piecesize
    pieces = {}
    for group_num, group in enumerate(groups):
        num = int(group[0][:-1].split(' ')[1])
        piece = group[1:]
        pieces[num] = []
        for flips in range(2):
            for rots in range(4):
                if group_num != 0 or (flips == 0 and rots == 0):
                    # don't flip or rotate one piece to avoid
                    # multiple flipped or rotated solutions.
                    pieces[num] += [list(piece)]
                rotate(piece)
            flip(piece)
        remain += [num]
    pieces[0] = [dummy]*8
    search([], remain)
