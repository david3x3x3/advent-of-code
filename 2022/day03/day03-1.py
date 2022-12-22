import sys

total = 0
with open(sys.argv[1]) as fp:
    for line in fp.readlines():
        line = line.strip()
        x = len(line)//2
        print(line)
        c = list(set.intersection(set(line[:x]), set(line[x:])))[0]
        if c >= 'a':
            total = total + ord(c) - ord('a') + 1
        else:
            total = total + ord(c) - ord('A') + 27
print(total)
