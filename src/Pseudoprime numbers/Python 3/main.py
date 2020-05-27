class Prime:

    MEM = {}

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        if n < 4:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        if n < 25:
            return True
        if n not in Prime.MEM:
            i=5
            while i*i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    Prime.MEM[n] = False
                    return False
                i += 6
            Prime.MEM[n] = True
        return Prime.MEM[n]

def mod_pow(a,b,mod):
    res = 1
    while b > 0:
        if b&1:
            res = (res * a) % mod
        a = (a * a) % mod
        b = b // 2
    return res % mod

def get_input():
    while True:
        p,a = map(int,input().split())
        if p == a == 0:
            break
        yield p,a

def is_base_a_pseudoprime(p,a):
    return mod_pow(a,p,p) == a and not Prime.is_prime(p)

def main():
    yes,no = 'yes','no'
    print('\n'.join(yes if is_base_a_pseudoprime(p,a) else no for p,a in get_input()))

if __name__ == "__main__":
    main()