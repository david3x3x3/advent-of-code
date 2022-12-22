import sys

with open(sys.argv[1]) as fp:
    lines = [line.strip() for line in fp.readlines()] + ['']

print(lines)

total = 0
totals = []
most = 0

for s in lines:
    if s == '':
        totals += [total]
        if total > most:
            most = total
        total = 0
        print('')
    else:
        old = total
        total += int(s)
        print('%d + %s = %d' % (old, s, total))

print(sorted(totals))
print(most)
