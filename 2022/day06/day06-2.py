import sys

with open(sys.argv[1]) as fp:
    for line in fp.readlines():
        line = line.strip()
        print(line)
        buf = list(line[:14])
        n = 14
        while n < len(line):
            #print(buf)
            dup = False
            for i in range(14):
                for j in range(i+1, 14):
                    if buf[i] == buf[j]:
                        dup = True
            if not dup:
                print("dup")
                break
            buf += line[n]
            del(buf[0])
            n += 1
        print(n)
        
