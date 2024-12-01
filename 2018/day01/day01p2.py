import sys

def make_groups(lines):
    groups = []
    prev = 0
    for line_num, line in enumerate(lines + ['']):
        if line == "":
            groups += [lines[prev:line_num]]
            prev = line_num + 1
    return groups

if __name__ == '__main__':
    lines = open(sys.argv[1]).read().strip().split('\n')
    reached = set()
    done = False
    total = 0
    while not done:
        for line in lines:
            if total not in reached:
                reached.add(total)
            else:
                done = True
                break
            if line[0] == '-':
                total -= int(line[1:])
            else:
                total += int(line[1:])
    print(total)
    
