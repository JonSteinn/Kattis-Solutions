from math import e, pi, log

LG2 = log(2)
LGPI = log(pi)

def log_of_sn(n):
    lgn = log(n)
    return (LG2 + LGPI + lgn)/2 + n*(lgn-1)

def log_fact(n):
    return sum(log(i) for i in range(2,n+1))

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        ratio = e**(log_fact(n) - log_of_sn(n))
        print('%.8f' % ratio)

if __name__ == "__main__":
    main()