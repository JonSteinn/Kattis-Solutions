from math import gcd

def cuts(m,n):
    g = gcd(m,n)
    if g > 1:
        return g*cuts(m//g, n//g)
    return (n&1)*(m&1)

def main():
    print(cuts(*map(int,input().split())))

if __name__ == "__main__":
    main()
