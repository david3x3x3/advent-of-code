import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    data = [line.strip().split(')') for line in fp.readlines()]

def path(p):
    if p == 'COM':
        return ['COM']
    return path(d[p]) + [p]

d = {}
for o in data:
    d[o[1]] = o[0]
print(d)
ans1 = 0
for p in d:
    pa = path(p)
    ans1 += len(pa)-1
p1 = path('YOU')
p2 = path('SAN')
print(p1)
print(p2)
while p1[0] == p2[0]:
    p1 = p1[1:]
    p2 = p2[1:]
print(p1)
print(p2)
ans2 = len(p1)-1 + len(p2)-1
print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')
