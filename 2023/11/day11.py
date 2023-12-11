import sys

lines = open(sys.argv[1]).read().strip().split('\n')
for part in range(1, 3):
    extra = 1 if part == 1 else 999999
    points = []
    for line_num, line in enumerate(lines):
        for ch_num, ch in enumerate(line):
            if ch == '#':
                points += [[line_num, ch_num]]
    sizes = [line_num + 1, ch_num + 1]
    for axis in range(2):
        n = 0
        while n < sizes[axis]:
            if n not in [p[axis] for p in points]:
                for p in points:
                    p[axis] += extra if p[axis] > n else 0
                sizes[axis] += extra
                n += extra
            n += 1
    answer = 0
    for n, p1 in enumerate(points[:-1]):
        for p2 in points[n+1:]:
            answer += abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    print(f'answer{part} = {answer}')
