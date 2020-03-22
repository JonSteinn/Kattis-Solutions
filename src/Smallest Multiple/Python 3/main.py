import sys
from math import gcd

def lcm_two(a,b):
    return a*b//gcd(a,b)

def lcm(many):
    try:
        a = next(many)
        b = next(many)
        curr = lcm_two(a,b)
    except StopIteration:
        return a
    while True:
        try:
            curr = lcm_two(curr, next(many))
        except StopIteration:
            return curr

def main():
    for line in sys.stdin:
        print(lcm(map(int, line.split())))

if __name__ == "__main__":
    main()