lis = [1, 1000, 12, 3, 22, 10, 8, 3]
ind = {
    'thou': 0, 'th': 0,
    'inch': 1, 'in': 1,
    'foot': 2, 'ft': 2,
    'yard': 3, 'yd': 3,
    'chain': 4, 'ch': 4,
    'furlong': 5, 'fur': 5,
    'mile': 6, 'mi': 6,
    'league': 7, 'lea': 7
}

s = input().split()
val = int(s[0])
f = ind[s[1]]
t = ind[s[3]]
if f == t:
    print(val)
elif f < t:
    p = 1
    while f != t:
        f += 1
        p /= lis[f]
    print(p * val)
else:
    p = 1
    while f != t:
        p *= lis[f]
        f -= 1
    print(val * p)
