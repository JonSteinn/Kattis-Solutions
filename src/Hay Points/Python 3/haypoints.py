m, n = tuple(map(lambda x: int(x), input().split()))
d = {}
for i in range(m):
    k = input().split()
    d[k[0]] = int(k[1])
for i in range(n):
    s = 0
    while True:
        _in = input().split()
        if len(_in) == 1 and _in[0] == '.':
            print(s)
            break
        s += sum(map(lambda t: d[t], filter(lambda z: z in d.keys(), _in)))