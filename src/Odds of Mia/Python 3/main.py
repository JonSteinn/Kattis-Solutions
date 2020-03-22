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

    def __repr__(self):
        return f'{self.a}' if self.b == 1 else f'{self.a}/{self.b}'

    def __str__(self):
        return f'{self.a}' if self.b == 1 else f'{self.a}/{self.b}'

def p1_wins(s0,s1,r0,r1):
    if r0 + r1 == 3:
        return False
    if s0+s1 == 3:
        return True
    if r0 == r1 and (s0 != s1 or s0 <= r0):
        return False
    if s0 == s1:
        return True
    return 10*max(s0,s1)+min(s0,s1) > 10*max(r0,r1)+min(r0,r1)

def probability(s0,s1,r0,r1):
    wins, total = 0,0
    # O(n^4) but n is at most 6 and 6^4 = 1296 => bruteforce
    for a in s0:
        for b in s1:
            for c in r0:
                for d in r1:
                    if p1_wins(a,b,c,d):
                        wins += 1
                    total += 1
    return Fraction(wins,total)

def convert_to_range(symbol):
    if symbol == '*':
        return range(1,7)
    else:
        return [int(symbol)]

def main():
    while True:
        s0,s1,r0,r1 = input().split()
        if s0 == '0':
            break
        s0 = convert_to_range(s0)
        s1 = convert_to_range(s1)
        r0 = convert_to_range(r0)
        r1 = convert_to_range(r1)
        print(probability(s0,s1,r0,r1))

if __name__ == "__main__":
    main()