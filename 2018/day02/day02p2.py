from collections import defaultdict
import sys

if __name__ == '__main__':
    lines = open(sys.argv[1]).read().strip().split('\n')
    done = False
    for w1 in lines:
        for w2 in lines:
            print(f'comparing {w1} and {w2}: ', end='')
            diffs = 0
            same = ''
            for i, c1 in enumerate(w1):
                if c1 != w2[i]:
                    diffs += 1
                else:
                    same += c1
            print(f'diffs = {diffs}')
            if diffs == 1:
                done = True
                break
        if done:
            break
print(f'same = {same}')
