import sys

total = 0
with open(sys.argv[1]) as fp:
    lines = fp.readlines()
    for i in range(len(lines)//3):
        contents = []
        for j in range(3):
            line = [lines[i*3+j].strip()]
            contents += line
            print(line)
        c = list(set.intersection(set(contents[0]),set(contents[1]),set(contents[2])))[0]

        # c = list(set.intersection(set(line[:x]), set(line[x:])))[0]
        if c >= 'a':
            total = total + ord(c) - ord('a') + 1
        else:
            total = total + ord(c) - ord('A') + 27
        print('')
print(total)
