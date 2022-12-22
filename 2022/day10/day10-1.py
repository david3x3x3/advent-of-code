import sys

cycle=0
x=1
score=0

with open(sys.argv[1]) as fp:
    for line in [x.strip().split(' ') for x in fp.readlines()]:
        #print(line)
        cmd = line[0]
        if cmd == 'noop':
            timer=1
        elif cmd == 'addx':
            timer=2

        while timer > 0:
            cycle += 1
            timer -= 1
            if (cycle+20)%40 == 0:
                score += (cycle*x)
                print(cycle, x, cycle*x, score)
                if cycle == 220:
                    exit(0)
            
        if cmd == 'addx':
            x += int(line[1])
        #print(f'{line} complete')
    print(cycle, x)
