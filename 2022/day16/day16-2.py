import sys

graph = {}
useful = []

with open(sys.argv[1]) as fp:
    for line in fp.readlines():
        words = line.strip().split()
        node = {}
        flow = int(words[4].split('=')[1].replace(';',''))
        node['flow'] = flow
        node['next'] = [w.strip(',') for w in words[9:]]
        node['dists'] = {}
        graph[words[1]] = node
        if flow > 0:
            useful += [words[1]]

for valve1 in graph.keys():
    node = graph[valve1]
    for valve2 in graph.keys():
        if valve1 == valve2:
            dist = 0
        else:
            dist = -1
        node['dists'][valve2] = dist

for current in graph.keys():
    depth=0
    done=False
    while not done:
        done=True
        for valve1 in graph.keys():
            node = graph[valve1]
            if node['dists'][current] == depth:
                for valve2 in node['next']:
                    node2 = graph[valve2]
                    if node2['dists'][current] < 0:
                        done=False
                        node2['dists'][current] = depth+1
        depth += 1

for valve in graph:
    print(graph[valve])

best = 0

def search(time_left, path, desc, score, loc):
    global best
    
    if time_left[1] > time_left[0]:
        mover = 1
    else:
        mover = 0
    if time_left[mover] == 0:
        if score >= best:
            print(f'{score} - {desc}')
            best = score
        return
        
    loc_node = graph[loc[mover]]
    dead_end = True
    for valve in useful:
        dist = loc_node['dists'][valve]
        time_left2 = list(time_left)
        time_left2[mover] -= (dist + 1)
        if valve not in path and time_left2[mover] > 0:
            loc2 = list(loc)
            loc2[mover] = valve
            search(time_left2, path + [valve], desc + '%s%s ' % ('he'[mover], valve), score + time_left2[mover]*graph[valve]['flow'], loc2)
            dead_end = False
    if dead_end:
        time_left2 = list(time_left)
        time_left2[mover] = 0
        search(time_left2, path, desc, score, loc)

search([26,26], [], '', 0, ['AA','AA'])
print(best)
