import sys

def mod_pow(a,b,mod):
    res = 1
    while b > 0:
        if b&1:
            res = (res * a) % mod
        a = (a * a) % mod
        b = b // 2
    return res % mod

def main():
    for line in sys.stdin:
        a,op,b = line.split()
        if op=='+':
            print((int(a[-4:]) + int(b[-4:]))%10000)
        elif op=='*':
            print((int(a[-4:]) * int(b[-4:]))%10000)
        else:
            print(mod_pow(int(a),int(b),10000))

if __name__ == "__main__":
    main()