import sys
from itertools import permutations

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
for perm in permutations(list(range(5))):
    print(perm)
    amps = []
    for i in perm:
        amps += [{ 'mem': list(mem0), 'pc': 0, 'inp': [i], 'running': True }]
    amps[0]['inp'] += [0]
    output = []
    while True in [a['running'] for a in amps]:
        for amp_num, a in enumerate(amps):
            if not a['running']:
                continue
            mem = a['mem']
            pc = a['pc']
            inp = a['inp']
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
                    if len(inp) == 0:
                        # run same command when there is input
                        break
                    mem[args[0]] = inp[0]
                    del inp[0]
                    pc += (len(args)+1)
                elif cmd == 4: # OUT
                    print(f'OUT = {args[0]} from {amp_num} to {amp_num+1}')
                    val = args[0]
                    if amp_num < 4:
                        amps[amp_num+1]['inp'] += [val]
                    else:
                        output += [val]
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
                    a['running'] = False
                    break
                else:
                    print(f'unknown cmd: {mem[pc]}')
                    sys.exit(1)
    print(f'perm {perm} output {output}')
    res += output
print(max(res))
