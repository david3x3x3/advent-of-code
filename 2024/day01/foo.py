lines = open('input.txt').read().strip().split('\n')
lists = [sorted(list(map(int,[l.split(' ')[n] for l in lines]))) for n in (0, -1)]
print(sum([abs(i1 - lists[1][i]) for i, i1 in enumerate(lists[0])]))
print(sum([lists[1].count(i1)*i1 for i1 in lists[0]]))
