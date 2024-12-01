from collections import defaultdict
import sys

if __name__ == '__main__':
    lines = open(sys.argv[1]).read().strip().split('\n')
    twos = 0
    threes = 0
    for line in lines:
        two = 0
        three = 0
        print(line)
        counts = defaultdict(int)
        for c in line:
            counts[c] += 1
        for k in counts:
            if counts[k] == 2:
                two = 1
            if counts[k] == 3:
                three = 1
        twos += two
        threes += three
    print(twos*threes)
    
