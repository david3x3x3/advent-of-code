import sys

count = 0
with open(sys.argv[1]) as fp:
    for line in fp.readlines():
        line = line.strip();
        elves = line.split(',')
        a = list(map(int,elves[0].split('-')))
        b = list(map(int,elves[1].split('-')))
        print(line)
        a_s = set(range(a[0],a[1]+1))
        print(a_s)
        b_s = set(range(b[0],b[1]+1))
        print(b_s)
        if len(set.intersection(set(a_s),set(b_s))) > 0:
            count += 1
        print('')
print(count)
