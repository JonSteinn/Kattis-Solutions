def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def mod_inv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m

def factor_2_prime(n):
    if n%2 == 0:
        return 2,n//2
    if n % 3 == 0:
        return 3,n//3
    i=5
    while i < 1000:
        if n % i == 0:
            return i, n//i
        if n % (i + 2) == 0:
            return i+2,n//(i+2)
        i += 6
    return -1

def find_d(n,e):
    phi_n = (lambda f1,f2: (f1-1)*(f2-1))(*factor_2_prime(n))
    return mod_inv(e,phi_n)

def main():
    for _ in range(int(input())):
        print(find_d(*map(int,input().split())))

if __name__ == "__main__":
    main()