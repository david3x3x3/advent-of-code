import sys

with open(sys.argv[1]) as fp:
    total = 0
    for line in fp.readlines():
        line = line.strip()
        words = line.split(' ')
        x = ord(words[1])-88
        total = total + x*3 + (ord(words[0])+x)%3+1
        print(line, ord(words[0]), ord(words[1]))
print(total)
