import sys

with open(sys.argv[1]) as fp:
    mem = list(map(int, fp.readlines()[0].split(',')))

mem[1] = 12
mem[2] = 2
pc = 0

while True:
    if mem[pc] == 1: # add
        _a = mem[pc+1]
        _b = mem[pc+2]
        _c = mem[pc+3]
        a = mem[_a]
        b = mem[_b]
        print(f'{pc}: {a}+{b} = {a+b} stored in {_c}')
        mem[_c] = a + b
        pc += 4
    elif mem[pc] == 2: # multiply
        _a = mem[pc+1]
        _b = mem[pc+2]
        _c = mem[pc+3]
        a = mem[_a]
        b = mem[_b]
        print(f'{pc}: {a}*{b} = {a+b} stored in {_c}')
        mem[_c] = a * b
        pc += 4
    elif mem[pc] == 99: # halt
        break
print(mem[0])
