n, d = int(input()), int(input())
songs = [set() for i in range(n + 1)]

for i in range(d):
    lis = list(map(int, input().split()))[1:]
    if 1 in lis:
        for j in lis:
            songs[j].add(i)
    else:
        new_set = set()
        for j in lis:
            new_set |= songs[j]
        for j in lis:
            songs[j] = new_set.copy()

list(map(lambda y: print(y[0]), filter(lambda z: z[0] > 0 and len(z[1]) == len(songs[1]), enumerate(songs))))