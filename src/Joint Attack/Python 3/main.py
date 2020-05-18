from math import gcd

class Fraction:
    def __init__(self, a=0,b=1):
        if b < 0:
            a = -a
            b = -b
        d = gcd(a,b)
        self.a = a // d
        self.b = b // d

    def __add__(self, other):
        return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)

    def __neg__(self):
        return Fraction(-self.a, self.b)

    def __sub__(self,other):
        return self + (-other)

    def __mul__(self,other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __truediv__(self,other):
        return Fraction(self.a * other.b, self.b * other.a)

    def inverse(self):
        return Fraction(self.b,self.a)

    def __repr__(self):
        return f'{self.a}' if self.b == 1 else f'{self.a}/{self.b}'

    def __str__(self):
        return f'{self.a}' if self.b == 1 else f'{self.a}/{self.b}'

def main():
    input() # Dump
    lis = list(map(lambda z: Fraction(int(z)), input().split()))
    f = lis.pop()
    while lis:
        f = lis.pop() + f.inverse()
    print(f)

if __name__ == "__main__":
    main()