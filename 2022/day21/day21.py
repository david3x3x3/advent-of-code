import sys

monkeys = {}

with open(sys.argv[1]) as fp:
    for line in fp.readlines():
        words = line.strip().split()
        monkey = { 'formula': [] }
        if words[1].isnumeric():
            monkey['value'] = int(words[1])
        else:
            monkey['formula'] = words[1:]
        monkeys[words[0].strip(':')] = monkey

while 'value' not in monkeys['root']:
    for k in monkeys:
        m = monkeys[k]
        print(f'm = {m}')
        if 'value' in m:
            continue
        else:
            if 'value' in monkeys[m['formula'][0]] and \
               'value' in monkeys[m['formula'][2]]:
                v1 = monkeys[m['formula'][0]]['value']
                v2 = monkeys[m['formula'][2]]['value']
                op = m['formula'][1]
                if op == '+':
                    m['value'] = v1 + v2
                elif op == '-':
                    m['value'] = v1 - v2
                elif op == '*':
                    m['value'] = v1 * v2
                elif op == '/':
                    m['value'] = v1 // v2
print(monkeys['root'])
