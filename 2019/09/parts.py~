import sys

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
    99: ['HALT', 0],
}
    
res = []
for part in range(2):
    mem = list(mem0)
    pc = 0
    output = []
    while True:
        # print(f'mem[{pc}] = {mem[pc]}')
        cmd = mem[pc] % 100
        flags = mem[pc] // 100
        args = mem[pc+1:pc+1+cmds[cmd][1]]
        for i in range(len(args)):
            if flags % 10 == 0 and i != cmds[cmd][2]:
                args[i] = mem[args[i]]
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
        elif mem[pc] == 99: # halt
            res += [output[-1]]
            break
        else:
            print(f'unknown cmd: {mem[pc]}')
            sys.exit(1)
print(f'answers = {res}')
