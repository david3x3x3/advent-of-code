import sys

with open(sys.argv[1]) as fp:
    #ints = [(i, int(s.strip())) for i, s in enumerate(fp.readlines())]
    ints = [(i, int(s.strip())*811589153) for i, s in enumerate(fp.readlines())]

mylen = len(ints)

#print(f'lines = {ints}')

for rounds in range(10):
    for i in range(mylen):
        #print('')
        #print([x[1] for x in ints])
        #print(ints)
        for pos, k in enumerate(ints):
            if i == k[0]:
                break
        val = ints[pos]
        count = val[1]
        count = count % (mylen-1)
        if count == 0:
            continue
        newpos = pos + count%mylen
        if newpos < 0:
            newpos = mylen-1+newpos
        #print(f"newpos {newpos}")
        elif newpos >= mylen:
            newpos = newpos % (mylen-1)
        #print(f'pos = {pos} newpos = {newpos} count = {count} num = {ints[pos][1]}')
        del(ints[pos])
        ints.insert(newpos, val)

    #print(ints)
    #print([x[1] for x in ints])

for pos, k in enumerate(ints):
    if 0 == k[1]:
        break
    
res = [ints[(i*1000+pos) % mylen][1] for i in range(1,4)]
print(res, sum(res))
