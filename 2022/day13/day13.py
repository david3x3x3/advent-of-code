import sys, functools

with open(sys.argv[1]) as fp:
    lines = [x.strip() for x in fp.readlines()]

#print('\n'.join(lines))

def mycmp(v1, v2):
    #print(f'{" "*depth}comparing {v1} to {v2}')
    if isinstance(v1, int):
        if isinstance(v2, int):
            if v1 < v2:
                #print(' '*depth+'Left side is smaller')
                return -1
            elif v1 == v2:
                return 0
            else:
                #print(' '*depth+'Right side is smaller')
                return 1
        else:
            return mycmp([v1], v2)
    elif isinstance(v2, int):
        res = mycmp(v1, [v2])
        return res
    # if we made it here, both args are lists
    for i in range(max(len(v1),len(v2))):
        if i >= len(v1):
            #print(' '*depth+'Left side ran out of items')
            return -1
        if i >= len(v2):
            #print(' '*depth+'Right side ran out of items')
            return 1
        res = mycmp(v1[i], v2[i])
        if res != 0:
            return res
    return 0

ok = []

dividers = ['[[2]]','[[6]]']
lines2 = list(dividers)

for i in range((len(lines)+1)//3):
    exp1 = lines[i*3]
    lines2 += [exp1]
    var1 = eval(exp1)
    
    exp2 = lines[i*3+1]
    lines2 += [exp2]
    var2 = eval(exp2)

    if mycmp(var1, var2) < 0:
        ok += [i+1]

print('part 1:')
#print(ok)
print(sum(ok))

print('part 2:')

def mycmp2(a,b):
    return mycmp(eval(a), eval(b))

lines2 = sorted(lines2, key=functools.cmp_to_key(mycmp2))
#print('\n'.join(map(str,lines2)))
#print('')
res = 1
for i, v in enumerate(lines2):
    if v in dividers:
        res *= (i+1)
print(res)
