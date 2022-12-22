import sys

with open(sys.argv[1]) as fp:
    lists = []
    while True:
        line = fp.readline()
        line = line.replace("\n", "")
        if len(lists) == 0:
            for i in range((len(line)+1)//4+1):
                lists += [[],]
        if line[1] == '1':
            fp.readline()
            break
        print('|%s|' % line)
        for i in range((len(line)+1)//4):
            c = line[i*4+1]
            if c != ' ':
                lists[i+1] = [c] + lists[i+1]
    print(lists[1:])
    for line in fp.readlines():
        print(line)
        words = line.strip().split(' ')
        count = int(words[1])
        src = lists[int(words[3])]
        dest = lists[int(words[5])]
        dest += src[-count:]
        del(src[-count:])
        print(lists[1:])
        print('')

print(''.join(x[-1] for x in lists[1:]))
