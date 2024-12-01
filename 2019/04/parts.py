a = 206938
b = 679128
count1 = 0
count2 = 0
for p in range(a, b+1):
    ps = list(map(int,str(p)))
    d = [ps[n+1] - ps[n] for n in range(len(ps)-1)]
    if 0 not in d or True in [x < 0 for x in d]:
        continue
    count1 += 1
    ok = False
    for i, n in enumerate(d):
        if n == 0 and (i==0 or d[i-1] != 0) and (i==4 or d[i+1] != 0):
            ok = True
    if ok:
        count2 += 1
    print(count1, count2, p, d, ok)
print(f'part 1: {count1}')
print(f'part 2: {count2}')
