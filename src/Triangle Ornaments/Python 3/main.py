from math import sqrt

print('%.4f' % sum((lambda _a,_b,c: c if _b == _a else (lambda a,b: 2*sqrt((c/2)**2 - ((a**2/2 + b**2/2 - c**2/4 - (b**2 - (c/2)**2))/(2*sqrt(a**2/2 + b**2/2 - c**2/4)))**2))(max(_a,_b),min(_a,_b)))(*map(int,input().split())) for _ in range(int(input()))))

# See C version for explanation...