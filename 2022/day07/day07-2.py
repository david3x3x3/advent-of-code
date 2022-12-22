import sys

with open(sys.argv[1]) as fp:
    lines = [x.strip().split(' ') for x in fp.readlines()]

i=0
sizes = {'/': 0}
wd = []
while i < len(lines):
    cmd = lines[i][1]
    #print(lines[i])
    if cmd == 'cd':
        dir = lines[i][2]
        if dir == "/":
            wd = []
        elif dir == "..":
            del(wd[-1])
        else:
            wd += [dir]
    elif cmd == 'ls':
        while True:
            i += 1
            if i == len(lines) or lines[i][0] == '$':
                break
            elif lines[i][0] == 'dir':
                path = '/' + '/'.join(wd + [lines[i][1]])
                if path not in sizes:
                    sizes[path] = 0
            else:
                path = ''
                for j in [''] + wd:
                    if j == '':
                        path = '/'
                    elif len(path) == 1:
                        path = path + j
                    else:
                        path = path + '/' + j
                    sizes[path] += int(lines[i][0])
        i -= 1
    i += 1

target = sizes['/'] - 40000000
print(f'target = {target}')
smallest = 70000000
minpath = 'null'
for k in sizes:
    s = sizes[k]
    if s >= target and s < smallest:
        smallest = s
        minpath = k
print(minpath, smallest)
