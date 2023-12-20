import sys, math
graph = {}
for line in open(sys.argv[1]).read().strip().split('\n'):
    parts = line.split(' -> ')
    graph[parts[0]] = parts[1].split(', ')
res = []
for m in graph['broadcaster']:
    nextl = [m]
    bin = ''
    while len(nextl) > 0:
        m2 = nextl[0]
        g = graph['%'+m2]
        bin = ('1' if len(g) == 2 or '%'+g[0] not in graph else '0') + bin
        nextl = [next_ for next_ in graph['%'+m2] if '%' + next_ in graph]
    res += [int(bin, 2)]
print(math.lcm(*res))
