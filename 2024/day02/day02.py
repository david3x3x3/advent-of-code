def is_safe(lev):
    inc = 1 if lev[1] > lev[0] else -1
    for i in range(len(lev)-1):
        diff = (lev[i+1]-lev[i])*inc
        if diff < 1 or diff > 3:
            return False
    return True

if __name__ == '__main__':
    lines = open('input.txt').read().strip().split('\n')
    for part in range(2):
        count = 0
        for line in lines:
            levels = list(map(int,line.split(' ')))
            safe = is_safe(levels)
            if not safe and part > 0:
                for i in range(len(levels)):
                    levels2 = list(levels)
                    del levels2[i]
                    if is_safe(levels2):
                        safe = True
                        break
            if safe:
                count += 1
        print(count)
