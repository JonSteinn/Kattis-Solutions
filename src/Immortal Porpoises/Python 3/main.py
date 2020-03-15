mod = 10**9

def fibonacci(n):
    if n == 0:
        return (0, 1)
    else:
        c, d, _d = (lambda a,b: (a * (b * 2 - a), *(lambda z: (z, z % mod))(a * a + b * b)))(*fibonacci(n // 2))
        if n % 2 == 0:
            return (c % mod, _d)
        else:
            return (_d, (c + d) % mod)

for _ in range(int(input())):
    a,b = map(int,input().split())
    print(f'{a} {fibonacci(b)[0]}')