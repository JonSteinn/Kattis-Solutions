first = True
while True:
    n,_ = tuple(map(int, input().split()))
    if n == 0:
        break
    elif not first:
        print()
    print((lambda x: '\n'.join(''.join(x) for x in zip(*map(tuple, x))))(sorted([''.join(x) for x in zip(*map(tuple, (input() for _ in range(n))))], key=lambda s: s.lower())))
    first = False