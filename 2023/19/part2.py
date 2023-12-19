import sys
import re
from copy import deepcopy
import numpy as np


def make_groups(lines):
    groups = []
    prev = 0
    for line_num, line in enumerate(lines + ['']):
        if line == "":
            groups += [lines[prev:line_num]]
            prev = line_num + 1
    return groups


lines = open(sys.argv[1]).read().strip().split('\n')
groups = make_groups(lines)
answer = 0
workflows = {}
varls = {}
for line in groups.pop(0):
    words = line.split('{')
    workflows[words[0]] = words[1][:-1].split(',')
    varls[words[0]] = []
varls['in'] += [{'x': [1, 4000],
                 'm': [1, 4000],
                 'a': [1, 4000],
                 's': [1, 4000]}]
varls['A'] = []
varls['R'] = []
while True:
    print('')
    done = True
    for workflow_id, varl in varls.items():
        if len(varl) > 0:
            done = False
            vars = varl.pop(0)
            break
    if done:
        break
    print(f'workflow id = {workflow_id}')
    print(vars)
    if workflow_id == 'A':
        print('  accepted')
        prod = 1
        for v in vars.values():
            prod *= v[1]-v[0]+1
        answer += prod
        continue
    if workflow_id == 'R':
        print('  rejected')
        continue
    workflow = workflows[workflow_id]
    for rule in workflow:
        print(f'rule = {rule}')
        rp = re.split('<|>|:', rule)
        if len(rp) == 1:
            print(f'  sending all to {rp[0]}')
            varls[rp[0]] += [vars]
            break
        vrange = vars[rp[0]]
        if '<' in rule:
            if vrange[0] < int(rp[1]):
                if vrange[1] < int(rp[1]):
                    print(f'  < sending all to {rp[2]}')
                    varls[rp[2]] += [vars]
                    break
                else:
                    vars2 = deepcopy(vars)
                    vars2[rp[0]][1] = int(rp[1])-1
                    varls[rp[2]] += [vars2]
                    vrange[0] = int(rp[1])
                print(f'  after <: {vars}')
            else:
                print('  no vars affected')
        elif '>' in rule:
            if vrange[1] > int(rp[1]):
                if vrange[0] > int(rp[1]):
                    print(f'  > sending all to {rp[2]}')
                    varls[rp[2]] += [vars]
                    break
                else:
                    vars2 = deepcopy(vars)
                    vars2[rp[0]][0] = int(rp[1])+1
                    varls[rp[2]] += [vars2]
                    vrange[1] = int(rp[1])
                    print(f'  after >: {vars}')
            else:
                print('  no vars affected')
print(f'answer = {answer}')
