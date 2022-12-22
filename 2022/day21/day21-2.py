import sys

monkeys = {}

with open(sys.argv[1]) as fp:
    for line in fp.readlines():
        words = line.strip().split()
        monkey = { 'formula': [] }
        if words[1].isnumeric():
            monkey['value'] = int(words[1])
            if words[0] == 'humn:':
                monkey['formulastr'] = 'x'
                monkey['undo'] = []
            else:
                monkey['formulastr'] = words[1]
        else:
            monkey['formula'] = words[1:]
        monkeys[words[0].strip(':')] = monkey

monkeys['root']['formula'][1] = '='

def doundo(v1, ops):
    #print(f'doundo {v1}, {ops}')
    for op, v2 in ops:
        if op == '+':
            v1 += v2
        elif op == '-':
            v1 -= v2
        elif op == '*':
            v1 *= v2
        elif op == '/':
            v1 //= v2
        else:
            print(f'unknown operator to undo: {op}')
            exit(1)
    print(f'x = {v1}')

while 'value' not in monkeys['root']:
    for k in monkeys:
        m = monkeys[k]
        #print(f'm = {m}')
        if 'value' in m:
            continue
        else:
            if 'value' in monkeys[m['formula'][0]] and \
               'value' in monkeys[m['formula'][2]]:
                v1 = monkeys[m['formula'][0]]['value']
                f1 = monkeys[m['formula'][0]]['formulastr']
                v2 = monkeys[m['formula'][2]]['value']
                f2 = monkeys[m['formula'][2]]['formulastr']
                op = m['formula'][1]
                if op == '+':
                    m['value'] = v1 + v2
                elif op == '-':
                    m['value'] = v1 - v2
                elif op == '*':
                    m['value'] = v1 * v2
                elif op == '/':
                    m['value'] = v1 // v2
                elif op == '=':
                    print(f'{f1} = {f2}')
                    if f1[0].isnumeric():
                        doundo(int(f1), monkeys[m['formula'][2]]['undo'])
                    else:
                        doundo(int(f2), monkeys[m['formula'][0]]['undo'])
                    exit(0)
                    #m['value'] = v1 // v2
                if f1[0].isnumeric() and f2[0].isnumeric():
                    m['formulastr'] = str(m['value'])
                else:
                    m['formulastr'] = f'({f1} {op} {f2})'
                    if f1[0].isnumeric():
                        undo = monkeys[m['formula'][2]]['undo']
                        if op == '+':
                            m['undo'] = [['-', int(f1)]] + undo
                        elif op == '-':
                            m['undo'] = [['-', int(f1)]] + [['*', -1]] + undo
                        elif op == '*':
                            m['undo'] = [['/', int(f1)]] + undo
                        elif op == '/':
                            m['undo'] = [['~', int(f1)]] + undo # 1/x 
                    else:
                        undo = monkeys[m['formula'][0]]['undo']
                        if op == '+':
                            m['undo'] = [['-', int(f2)]] + undo
                        elif op == '-':
                            m['undo'] = [['+', int(f2)]] + undo
                        elif op == '*':
                            m['undo'] = [['/', int(f2)]] + undo
                        elif op == '/':
                            m['undo'] = [['*', int(f2)]] + undo
print(monkeys['root'])
