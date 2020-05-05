def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def mod_inv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m

def mod_eval(a, op, b, mod):
    _a,_b= int(a),int(b)
    if op == '+':
        return (_a+_b)%mod
    if op == '-':
        return (mod+_a-_b)%mod
    if op == '*':
        return (_a*_b)%mod
    inv = mod_inv(_b,mod)
    if inv == -1:
        return -1
    return (_a * mod_inv(_b,mod))%mod

def main():
    while True:
        n,t = map(int,input().split())
        if n == 0 and t == 0:
            break
        for _ in range(t):
            print(mod_eval(*input().split(), n))

if __name__ == "__main__":
    main()