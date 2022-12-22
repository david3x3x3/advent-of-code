import sys, math

minerals = ['ore', 'clay', 'obsidian', 'geode']

print(minerals)

best=0

def search(inv, robots, timeleft, matlist):
    global best
    #print(f'search({inv}, {robots}, {timeleft}, \'desc\')')
    found_any = False
    best_possible = inv[3]
    tmp_robots = list(robots)
    for i in range(timeleft):
        best_possible += tmp_robots[3]
        tmp_robots[3] += 1
    if best_possible > best:
        # prune the search if we can't beat the best score
        for new_type in reversed(range(4)):
            cost = costs[new_type]
            ok = True
            if new_type < 3 and robots[new_type] >= maxcosts[new_type]:
                # no use building this many of that kind of robot
                ok = False
            for i, subcost in enumerate(cost):
                if subcost > 0 and robots[i] == 0:
                    #print(f"no robot can make {minerals[i]} to make a {minerals[new_type]} robot")
                    ok = False
            if ok:
                #print(f'try making a {minerals[new_type]} robot')
                rounds = []
                for mat in range(3):
                    if costs[new_type][mat] > 0:
                        # how many rounds to produce the materials for this robot
                        rounds += [math.ceil((costs[new_type][mat]-inv[mat])/robots[mat])]
                    else:
                        rounds += [0]
                #print(f'rounds for each ingredient = {rounds}')
                rounds = max(rounds) + 1 # add extra round to build robot
                #print(f'rounds for all = {rounds}')
                if timeleft - rounds > 0:
                    inv2 = list(inv)
                    for mat in range(4):
                        inv2[mat] = inv2[mat] + robots[mat]*rounds - costs[new_type][mat]
                    robots[new_type] += 1
                    search(inv2, robots, timeleft-rounds, matlist + [minerals[new_type]])
                    robots[new_type] -= 1
                    found_any = True
    if not found_any:
        score = inv[3] + timeleft * robots[3]
        #print(f'{score} - {desc}', flush=True)
        if score > best:
            print(f"{score} - {' '.join(matlist)}", flush=True)
            best = score

res = 1
with open(sys.argv[1]) as fp:
    lineno = 1
    for line in fp.readlines():
        best = 0
        costs = []
        for i in range(4):
            costs += [[0,0,0]]
        line = line.strip()
        ints = [int(w) for w in line.split(' ') if w.isnumeric()]
        print(line)
        print(ints)
        costs[0] = [ints[0], 0, 0, 0]
        costs[1] = [ints[1], 0, 0, 0]
        costs[2] = [ints[2], ints[3], 0, 0]
        costs[3] = [ints[4], 0, ints[5], 0]
        print(f'costs = {costs}')
        maxcosts = [max([costs[j][i] for j in range(4)]) for i in range(4)]
        print(f'maxcosts = {maxcosts}')
        myinv = [0,0,0,0]
        myrobots = [1,0,0,0]
        search(myinv, myrobots, 32, [])
        print(lineno, best)
        res = res * best
        lineno += 1
        #if lineno > 3:
        #    break
print(f'res = {res}')
