lo,hi = (-1,1001)
for _ in range(int(input())):
    lo, hi = (lambda a,b: (max(lo,a), min(hi,b)))(*tuple(map(int, input().split())))
print('gunilla has a point' if lo <= hi else 'edward is right')