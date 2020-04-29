from math import log2 as lg, sqrt

class Func:
    n,p,s,v = map(float,input().split())
    sq2 = sqrt(2)
    lgn = lg(n)
    a = (n/(p*10**9))
    b = s/v

    @staticmethod
    def f(c):
        return Func.a * (Func.lgn)**(c*Func.sq2) + Func.b * (1+1/c)

    @staticmethod
    def g(c):
        return 1/(Func.a * (Func.lgn)**(c*Func.sq2) + Func.b * (1+1/c))

def find_c(l,r,d=10E-7):
    while abs(l-r) > d:
        c1 = l + (r-l)/3
        c2 = r - (r-l)/3
        if Func.g(c1) < Func.g(c2):
            l = c1
        else:
            r = c2
    return (l+r)/2

def main():
    c = find_c(0.1,100) # guessed range and precisin + trial&error
    print('%.6f %.6f' % (Func.f(c),c))


if __name__ == "__main__":
    main()