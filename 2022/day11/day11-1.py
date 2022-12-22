import sys, math

monkeys = []
with open(sys.argv[1]) as fp:
    for line in fp.readlines():
        line = line.rstrip()
        print(line)
        words = line.strip().split(' ')
        if words[0] == 'Monkey':
            monkey = { 'num': int(words[1].strip(':')), 'score': 0 }
            monkeys += [monkey]
        elif words[0] == 'Starting':
            monkey['items'] = [int(i.strip(',')) for i in words[2:]]
        elif words[0] == 'Operation:':
            monkey['op'] = words[3:]
        elif words[0] == 'If':
            monkey[words[1].strip(':')] = int(words[-1])
        elif words[0] == 'Test:':
            monkey['testdiv'] = int(words[-1])
        elif line == '':
            del(monkey)
        else:
            print('unknown syntax')
            #exit(1)
        #print(monkey)
print('\n'.join(map(str,monkeys)))

for round in range(20):
    for monkey in monkeys:
        print(f'monkey #{monkey["num"]}')
        while len(monkey['items']):
            monkey['score'] += 1
            item = monkey['items'].pop(0)
            print(f' item {item}')
            a = monkey['op'][0]
            b = monkey['op'][2]
            if a == 'old':
                a = item
            else:
                a = int(a)
            if b == 'old':
                b = item
            else:
                b = int(b)
            if monkey['op'][1] == '+':
                item = a + b
            elif monkey['op'][1] == '*':
                item = a * b
            print(f' new worry level is {item}')
            item //= 3
            print(f' boredom worry level is {item}')
            if item % monkey['testdiv'] == 0:
                target = monkey['true']
            else:
                target = monkey['false']
            print(f' passing to monkey {target}')
            monkeys[target]['items'] += [item]
    print(f'round {round+1}:')
    print('\n'.join(map(str,monkeys)))

print(math.prod(sorted([m['score'] for m in monkeys])[-2:]))
