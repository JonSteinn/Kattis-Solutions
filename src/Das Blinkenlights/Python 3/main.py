from math import gcd

print('yes' if (lambda p,q,s: (p*q)//gcd(p,q) <= s)(*tuple(map(int,input().split()))) else 'no')