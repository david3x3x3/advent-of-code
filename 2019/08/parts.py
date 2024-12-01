import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    data = list(map(int, fp.readlines()[0].strip()))

width=25
height=6
layers = []
for l in range(len(data)//width//height):
    layers += [data[l*width*height:(l+1)*width*height]]
counts = []
for i, l in enumerate(layers):
    count = defaultdict(lambda: 0)
    for n in l:
        count[n] += 1
    counts += [dict(count)]
m = min([c[0] for c in counts])
c2 = [c for c in counts if c[0] == m][0]
print(f'part 1 = {c2[1] * c2[2]}')
msg = [' ']*width*height
for l in reversed(layers):
    for i, n in enumerate(l):
        if n == 0:
            msg[i] = '.'
        elif n == 1:
            msg[i] = '@'
print('part 2:')
print('\n'.join([''.join(msg[r*width:(r+1)*width]) for r in range(height)]))
