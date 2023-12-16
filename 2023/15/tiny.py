import sys, re, collections
myhash = lambda s, n=0: n if s == '' else myhash(s[1:], (n+ord(s[0]))*17 % 256)
steps = open(sys.argv[1]).read().strip().split(',')
print('part 1:', sum(myhash(s) for s in steps))
bs = collections.defaultdict(dict)
for step in steps:
    words = re.split('-|=', step)
    box = bs[myhash(words[0])]
    if len(words[1]) == 0:
        box.pop(words[0], None)
    else:
        box[words[0]] = int(words[1])
print('part 2:', sum((b+1)*(n+1)*l for b in bs for n, l in enumerate(bs[b].values())))
