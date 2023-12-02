import sys

if __name__ == '__main__':
    nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'zero', 'one',
            'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

    with open(sys.argv[1]) as fp:
        lines = [x.strip() for x in fp.readlines()]

    for part in range(1, 3):
        answer = 0
        for line in lines:
            minpos = len(line)
            maxpos = -1
            for i, v in enumerate(nums):
                if part == 1 and v == 'zero':
                    break
                pos = line.find(v)
                if pos >= 0 and pos < minpos:
                    minpos = pos
                    first = i % 10
                pos = line.rfind(v)
                if pos >= 0 and pos > maxpos:
                    maxpos = pos
                    last = i % 10
            answer += first*10 + last
        print(f'part{part} = {answer}')
