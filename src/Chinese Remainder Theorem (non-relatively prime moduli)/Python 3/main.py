def egcd(a, b):
    return (lambda g,p,q: (g,q-(b//a)*p,p))(*egcd(b%a, a)) if a else (b,0,1)

def crt(a,n,b,m):
    return (lambda g,p,q: ('no solution',) if (a-b)%g else (lambda lcd: (((a * m * q + b * n * p) // g) % lcd, lcd))((n*m)//g))(*egcd(n,m))

def main():
    for _ in range(int(input())):
        print(*crt(*map(int,input().split())))

if __name__ == "__main__":
    main()
