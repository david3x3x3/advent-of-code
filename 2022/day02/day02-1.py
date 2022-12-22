import sys

with open(sys.argv[1]) as fp:
    total = 0
    for line in fp.readlines():
        line = line.strip()
        words = line.split(' ')
        check = (6,0,3)[(ord(words[1])-ord(words[0]))%3]
        total = total + check + ord(words[1])-87
        print(line, check, ord(words[1])-87)
print(total)
