# this solves part 1 and 2

import sys, time


def split_plan(plan, mid_len):
    res = []
    for i in range(0, len(plan)):
        left = plan[:i]
        right = plan[i:]
        if len(right) < mid_len:
            break
        mid = right[:mid_len]
        right = right[mid_len:]
        res += [(left, mid, right)]
    return res


def search(plan, nums, do_print=False):
    global cache
    if (plan, tuple(nums)) in cache:
        return cache[(plan, tuple(nums))]
    if len(nums) == 0:
        if '#' in plan:
            return (0, plan)
        return (1, '.' * len(plan))
    elif plan == '':
        return (0, plan)
    mid_num_pos = len(nums)//2
    left_nums = nums[:mid_num_pos]
    mid_num = nums[mid_num_pos]
    right_nums = nums[mid_num_pos+1:]
    res = 0
    ex = ''
    for left_str, mid_str, right_str in split_plan(plan, mid_num):
        if '.' in mid_str:
            # skipping pos {pos} because of mid_str
            continue
        if len(left_str) > 0:
            if left_str[-1] == '#':
                # skipping pos because of left char
                continue
            left_str = left_str[:-1]
            left_add = '.'
        else:
            left_add = ''
        if len(right_str) > 0:
            if right_str[0] == '#':
                # skipping pos because of right char
                continue
            right_str = right_str[1:]
            right_add = '.'
        else:
            right_add = ''
        left_score, left_ex = search(left_str, left_nums)
        if left_score == 0:
            # no results on left, so don't check right
            continue
        right_score, right_ex = search(right_str, right_nums)
        if right_score == 0:
            continue
        ex2 = left_ex + left_add + '#' * mid_num + right_add + right_ex
        if ex == '':
            ex = ex2
        if do_print:
            print(f'     {ex2}', end='\r', flush=True)
            time.sleep(0.05)
        res += left_score * right_score
    if do_print:
        print(f'     {ex} {res}\n', flush=True)
        # time.sleep(0.5)
    cache[(plan, tuple(nums))] = (res, ex)
    return (res, ex)


if __name__ == '__main__':
    lines = open(sys.argv[1]).read().strip().split('\n')
    for part in range(2, 3):
        cache = {}
        print(f'\nPart {part}')
        answer = 0
        for line_num, line in enumerate(lines):
            if part == 1:
                mult = 1
            else:
                mult = 5
            words = line.split()
            plans = '?'.join([words[0]] * mult)
            counts = list(map(int, words[1].split(','))) * mult
            # print()
            print(f'{line_num:3d}: {plans}')
            res, ex = search(plans, counts, True)
            # print(f'{line_num}: {plans} = {res}')
            answer += res

        print(f'answer{part} = {answer}')
