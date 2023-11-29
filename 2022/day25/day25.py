import sys

with open(sys.argv[1]) as fp:
    lines = [s.strip() for s in fp.readlines()]

def to_snafu(n):
    res = []
    carry = 0
    while n > 0:
        digit = n%5 + carry
        n //= 5
        if digit > 2:
            digit -= 5
            carry = 1
        else:
            carry = 0
        res = [digit] + res
    if carry > 0:
        res = [carry] + res
    return ''.join(['=-012'[x+2] for x in res])

def from_snafu(s):
    return sum([('=-012'.index(c) - 2) * pow(5, i) for i, c in enumerate(reversed(s))])

total = 0
for num in lines:
    res = from_snafu(num)
    print(res, num)
    total += res
print(total)
print(to_snafu(total))
