import sys

with open(sys.argv[1]) as fp:
    nums = list(map(int, fp.readlines()))

total = 0
for num in nums:
    while num > 8:
        num = num // 3 - 2
        total += num
print(total)
