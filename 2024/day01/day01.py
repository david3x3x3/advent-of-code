import sys

if __name__ == '__main__':
    lines = open(sys.argv[1]).read().strip().split('\n')
    lists = [sorted(list(map(int,[l.split(' ')[n] for l in lines]))) for n in (0, -1)]
    total = 0
    for i, i1 in enumerate(lists[0]):
        total += abs(i1 - lists[1][i])
    print(f'part 1: {total}')
    total = 0
    for i1 in lists[0]:
        total += lists[1].count(i1)*i1
    print(f'part 2: {total}')
