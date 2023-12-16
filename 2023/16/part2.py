import sys

lines = open(sys.argv[1]).read().strip().split('\n')

dirs = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

redir = {'|': {'R': ['U', 'D'], 'L': ['U', 'D'], 'U': ['U'], 'D': ['D']},
         '/': {'R': ['U'], 'L': ['D'], 'U': ['R'], 'D': ['L']},
         '-': {'R': ['R'], 'L': ['L'], 'U': ['L', 'R'], 'D': ['L', 'R']},
         '\\': {'R': ['D'], 'L': ['U'], 'U': ['L'], 'D': ['R']},
         '.': {'R': ['R'], 'L': ['L'], 'U': ['U'], 'D': ['D']}}

answer1 = 0

grid = {}
for line_num, line in enumerate(lines):
    for ch_num, ch in enumerate(line):
        grid[(line_num, ch_num)] = ch
num_rows = line_num + 1
num_cols = ch_num + 1

start = []
for c1 in range(num_cols):
    start += [(-1, c1, 'D'), (num_rows, c1, 'U')]
for r1 in range(num_rows):
    start += [(r1, -1, 'R'), (r1, num_cols, 'L')]

best = 0
for b0 in start:
    beams = [b0]
    print(f'start = {b0} ', end='')
    covered = set()
    hist = set()
    while len(beams) > 0:
        if False:
            for r1 in range(num_rows):
                for c1 in range(num_cols):
                    if (r1, c1) in [(r2, c2) for (r2, c2, ch) in beams]:
                        print('o', end='')
                    else:
                        print(grid[(r1, c1)], end='')
                print('')
            print('')
            print(beams)
        beams2 = []
        for b in beams:
            dr, dc = dirs[b[2]]
            r2 = b[0]+dr
            c2 = b[1]+dc
            if (r2, c2) not in grid:
                continue
            covered.add((r2, c2))
            for ch in redir[grid[(r2, c2)]][b[2]]:
                if (r2, c2, ch) not in hist:
                    beams2 += [(r2, c2, ch)]
                    hist.add((r2, c2, ch))
        beams = beams2
    print(f'score = {len(covered)}')
    if len(covered) > best:
        best = len(covered)
print('Part 2', best)
