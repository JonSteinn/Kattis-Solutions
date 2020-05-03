"""
Suppose we have a fraction a/b and we are looking for all numbers k
such that a/b * k is k but with the first letter moved to the back.
Let k = c_0 * 10**0 + c_1 * 10**1 + ... + c_n * 10**n, that is, k is
some integer of length n+1 (in string form k is c_n...c_1c_0). Then
it must hold that
    a/b * k = c_n + (c_0*10**1 + c_1*10**2 + ... + c_[n-1]*10**n)
or
    a * k = b * (c_n + (c_0*10**1 + c_1*10**2 + ... + c_[n-1]*10**n))
          = b * (c_n + 10*(c_0*10**0 + c*10**1 + ... + c_[n-1]*10**[n-1]))
          = b * (c_n + 10*sum(c_i*10**i, i in [0,n-1])) + b*c_n*10**[n+1] - b*c_n*10**[n+1]
          = b * (c_n + 10*sum(c_i*10**i, i in [0,n]) - c_n*10**[n+1])
          = b * (c_n + 10*k - c_n * 10**[n+1])
          = b * c_n + b * 10 * k - b * c_n * 10**[n+1]
=> a * k - b * 10 * k = b * c_n - b * c_n * 10**[n+1]
=> k * (a - b*10) = b * c_n - b * c_n * 10**[n+1]
=> k = (b * c_n - b * c_n * 10**[n+1]) / (a-b*10)
     = b * c_n * (1 - 10**[n+1]) / (a-b*10)
     = b * c_n * (10**[n+1] - 1) / (10*b - a)

Now that k need to satisfy the above equation we have a small search space.
The first number of k is never 0 so they can take any value from {1,2,...,9}
and then there is the length n which is limited by the input. For each of them,
check if they are valid trick numbers for the fraction.
"""

from math import gcd

class Fraction:
    @staticmethod
    def construct_from_decimal_string(string):
        a,b = string.split('.')
        return Fraction(int(a+b), 10**len(b))

    def __init__(self, a, b):
        g = gcd(a,b)
        self.a = a//g
        self.b = b//g

class TrickNumbers:

    @staticmethod
    def is_trick_number(f,k):
        d,m = divmod(f.a*k,f.b)
        return m == 0 and k == int(f'{d % 10}{str(d)[:-1]}')

    @staticmethod
    def generate_all_tricks(f):
        # Constructed in ascending order so no need for sorting
        for n in range(8):
            for last in range(1,10):
                _n = f.b * last * (10**(n+1) - 1)
                _d = (10 * f.b - f.a)
                if _d == 0:
                    break
                k,rem = divmod(_n,_d)
                if rem != 0:
                    continue
                if TrickNumbers.is_trick_number(f,k):
                    yield k

def main():
    f = Fraction.construct_from_decimal_string(input())
    numbs = [tn for tn in TrickNumbers.generate_all_tricks(f)]
    if not numbs:
        print('No solution')
    else:
        for numb in numbs:
            print(numb)

if __name__ == "__main__":
    main()