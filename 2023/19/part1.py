import sys
import re


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
for line in groups.pop(0):
    words = line.split('{')
    workflows[words[0]] = words[1][:-1].split(',')
print(workflows)
for line in groups.pop(0):
    vars = {}
    for p in line[1:-1].split(','):
        p2 = p.split('=')
        vars[p2[0]] = int(p2[1])
    print(vars)
    done = False
    workflow_id = 'in'
    while not done:
        if workflow_id == 'A':
            print('accepted')
            answer += sum(vars.values())
            break
        if workflow_id == 'R':
            print('rejected')
            break
        workflow = workflows[workflow_id]
        print(f'workflow {workflow_id}: {workflow}')
        for rule in workflow:
            print(f'rule = {rule}')
            rule_parts = re.split('<|>|:', rule)
            if len(rule_parts) == 1:
                print(f'skipping to {rule_parts[0]}')
                workflow_id = rule_parts[0]
                break
            print(f'rule_parts = {rule_parts}')
            if '<' in rule:
                if vars[rule_parts[0]] < int(rule_parts[1]):
                    print(f'jumping to {rule_parts[2]}')
                    workflow_id = rule_parts[2]
                    break
            if '>' in rule:
                if vars[rule_parts[0]] > int(rule_parts[1]):
                    print(f'jumping to {rule_parts[2]}')
                    workflow_id = rule_parts[2]
                    break
print(f'answer = {answer}')
