# this was my original solution for part 1

import sys

lines = open(sys.argv[1]).read().strip().split('\n')


def score(puz):
    # print(f'score {puz}')
    res = ','.join(map(str, ([len(s) for s in puz.split('.') if s != ''])))
    return res


def search(puz, nums):
    # print(f'puz = {puz}, nums = {nums}')
    puzl = list(puz)
    for i, ch in enumerate(puz):
        if ch == '?':
            res = 0
            for ch2 in ('.', '#'):
                puzl[i] = ch2
                res += search(''.join(puzl), nums)
            return res
    if score(puz) == nums:
        # print(f'  {puz}')
        return 1
    return 0


answer1 = 0

for line in lines:
    print(line, flush=True)
    answer1 += search(*line.split())

print(f'answer1 = {answer1}')
