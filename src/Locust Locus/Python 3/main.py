from math import gcd
print(min((lambda a,b,c: a+b*c//gcd(b,c))(*map(int, input().split())) for _ in range(int(input()))))