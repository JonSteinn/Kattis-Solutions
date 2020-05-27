from math import sqrt

def twos(n, t):
    s = 1
    while n and not n&1:
        t.append(1<<s)
        n >>= 1
        s += 1
    return n

def threes(n,t):
    s = 3
    while n and n%3 == 0:
        t.append(s)
        n //= 3
        s *= 3
    return n

def remaining(n):
    yield 1
    if n != 1:
        yield n

    f, top,jump = 5, sqrt(n),2
    while f <= top:
        d,m = divmod(n,f)
        if not m:
            yield f
            if f != d:
                yield d
        f = f + jump
        jump = 2 if jump == 4 else 4

def divisors(n):
    two,three = [],[]
    n = twos(n,two)
    n = threes(n, three)
    
    for c in remaining(n):
        yield c
        for a in two:
            yield a*c
            for b in three:
                yield a*b*c
        for b in three:
            yield b*c

def main():
    print(' '.join(str(x-1) for x in sorted(divisors(int(input())))))

if __name__ == "__main__":
    main()