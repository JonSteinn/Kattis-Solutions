b,c,d,l = map(int, input().split())

found = False
for _b in range(0,1+l//b):
    for _c in range(0,1+l//c):
        x1 = _b * b + _c * c
        if x1 > l:
            break
        for _d in range(0,1+l//d):
            x2 = x1 + _d * d
            if x2 > l:
                break
            if x2 == l:
                print(f'{_b} {_c} {_d}')
                found = True

if not found:
    print('impossible')