import sys

cycle=0
x=1
score=0
output = ''

with open(sys.argv[1]) as fp:
    for line in [x.strip().split(' ') for x in fp.readlines()]:
        #print(f'starting {line}')
        cmd = line[0]
        if cmd == 'noop':
            timer=1
        elif cmd == 'addx':
            timer=2

        while timer > 0:
            cycle += 1
            timer -= 1
            if abs((cycle%40)-x-1) < 2:
                c = '@'
            else:
                c = ' '
            output += c
            #print(c, cycle, x)
            if cycle % 40 == 0:
                print(output)
                output = ''
            
        if cmd == 'addx':
            x += int(line[1])
        #print(f'{line} complete')
