import sys

with open(sys.argv[1]) as fp:
    mem0 = list(map(int, fp.readlines()[0].split(',')))

for noun in range(100):
    for verb in range(100):
        mem = list(mem0)
        mem[1] = noun
        mem[2] = verb
        pc = 0
        while True:
            if mem[pc] == 1: # add
                _a = mem[pc+1]
                _b = mem[pc+2]
                _c = mem[pc+3]
                a = mem[_a]
                b = mem[_b]
                # print(f'{pc}: {a}+{b} = {a+b} stored in {_c}')
                mem[_c] = a + b
                pc += 4
            elif mem[pc] == 2: # multiply
                _a = mem[pc+1]
                _b = mem[pc+2]
                _c = mem[pc+3]
                a = mem[_a]
                b = mem[_b]
                # print(f'{pc}: {a}*{b} = {a+b} stored in {_c}')
                mem[_c] = a * b
                pc += 4
            elif mem[pc] == 99: # halt
                break
        print(noun, verb, mem[0])
        if mem[0] == 19690720:
            sys.exit(0)
