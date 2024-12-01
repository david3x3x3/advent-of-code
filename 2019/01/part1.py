import sys

with open(sys.argv[1]) as fp:
    nums = list(map(int, fp.readlines()))

total = 0
for num in nums:
    num2 = num // 3 - 2
    total += num2
print(total)
