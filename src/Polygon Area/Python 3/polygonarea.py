while True:
    n = int(input())
    if n == 0:
        break
    print((lambda val: "CW {0}".format(-val) if val < 0 else "CCW {0}".format(val))((lambda v: sum([(lambda a, b: a[0]*b[1]-a[1]*b[0])(v[i], v[i+1]) for i in range(len(v) - 1)] + [(lambda a, b: a[0]*b[1]-a[1]*b[0])(v[-1], v[0])]) / 2)([tuple(map(lambda x: int(x), input().split())) for i in range(n)])))