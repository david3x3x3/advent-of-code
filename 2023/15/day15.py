import sys
from collections import defaultdict


def myhash(s):
    res = 0
    for ch in s:
        res = (res+ord(ch))*17 % 256
    return res


steps = open(sys.argv[1]).read().strip().split(',')

# part 1
answer1 = sum(myhash(s) for s in steps)

# part 2
boxes = defaultdict(list)
for step in steps:
    if step[-1] == '-':
        # delete
        s1 = step[:-1]
        hash1 = myhash(s1)
        boxes[hash1] = [lens for lens in boxes[hash1] if lens[0] != s1]
    elif '=' in step:
        # add/change
        s1, s2 = step.split('=')
        hash1 = myhash(s1)
        found = False
        for lens in boxes[hash1]:
            if lens[0] == s1:
                lens[1] = s2
                found = True
        if not found:
            boxes[hash1] += [[s1, s2]]
# for boxnum, box in enumerate(boxes):
#     if len(box):
#         print(f'{boxnum}: {box}')
answer2 = 0
for box_num in boxes:
    for lens_num, lens in enumerate(boxes[box_num]):
        answer2 += (box_num+1) * (lens_num+1) * int(lens[1])

print(f'answer1 = {answer1}')
print(f'answer2 = {answer2}')
