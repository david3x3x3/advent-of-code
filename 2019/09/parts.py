import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    mem0 = list(map(int, fp.readlines()[0].split(',')))

# name, num args, outarg
cmds = {
    1: ['ADD', 3, 2],
    2: ['MUL', 3, 2],
    3: ['IN', 1, 0],
    4: ['OUT', 1, -1],
    5: ['JMPT', 2, -1],
    6: ['JMPF', 2, -1],
    7: ['LT', 3, 2],
    8: ['EQ', 3, 2],
    9: ['RELB', 1, -1],
    99: ['HALT', 0],
}
    
mem = defaultdict(lambda: 0)
for addr, val in enumerate(mem0):
    mem[addr] = val
pc = 0
part = 0
output = []
relbase = 0
while True:
    print(f'mem[{pc}] = {mem[pc]}')
    cmd = mem[pc] % 100
    flags = mem[pc] // 100
    args = [mem[x] for x in range(pc+1, pc+1+cmds[cmd][1])]
    print(f'preargs = {args}')
    for i in range(len(args)):
        flag = flags % 10
        if flag == 0:
            args[i] = mem[args[i]]
        elif flag == 2:
            if i == cmds[cmd][2]:
                args[i] += relbase
            else:
                args[i] = mem[relbase + args[i]]
        flags //= 10
    print('trace', mem[pc], cmds[cmd][0], args)
    if cmd == 1: # add
        mem[args[2]] = args[0] + args[1]
        print(f'  {mem[args[2]]} -> {args[2]}')
        pc += (len(args)+1)
    elif cmd == 2: # multiply
        mem[args[2]] = args[0] * args[1]
        print(f'  {mem[args[2]]} -> {args[2]}')
        pc += (len(args)+1)
    elif cmd == 3: # IN
        mem[args[0]] = [1, 5][part]
        pc += (len(args)+1)
    elif cmd == 4: # OUT
        print(f'OUT = {args[0]}')
        output += [args[0]]
        pc += (len(args)+1)
    elif cmd == 5: # JMPT
        if args[0] != 0:
            pc = args[1]
        else:
            pc += (len(args)+1)
    elif cmd == 6: # JMPF
        if args[0] == 0:
            pc = args[1]
        else:
            pc += (len(args)+1)
    elif cmd == 7: # LT
        mem[args[2]] = 1 if args[0] < args[1] else 0
        pc += (len(args)+1)
    elif cmd == 8: # EQ
        mem[args[2]] = 1 if args[0] == args[1] else 0
        pc += (len(args)+1)
    elif cmd == 9: # RELB
        relbase += args[0]
        pc += (len(args)+1)
    elif mem[pc] == 99: # halt
        break
    else:
        print(f'unknown cmd: {mem[pc]}')
        sys.exit(1)
print(f'output = {output}')
