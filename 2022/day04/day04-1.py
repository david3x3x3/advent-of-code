import sys

count = 0
with open(sys.argv[1]) as fp:
    for line in fp.readlines():
        line = line.strip();
        elves = line.split(',')
        a = list(map(int,elves[0].split('-')))
        b = list(map(int,elves[1].split('-')))
        print(line)
        print(list(range(a[0],a[1]+1)))
        print(list(range(b[0],b[1]+1)))
        
        if (a[0] <= b[0] and a[1] >= b[1]) or \
           (a[0] >= b[0] and a[1] <= b[1]):
            print('yes')
            count += 1
print(count)
