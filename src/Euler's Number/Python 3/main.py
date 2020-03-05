from math import e

# This is accurate within 12 decimals for n>=15
factorial = [
    1,
    1,
    2,
    6,
    24,
    120,
    720,
    5040,
    40320,
    362880,
    3628800,
    39916800,
    479001600,
    6227020800,
    87178291200
]

def main():
    n = int(input())
    print("%.12f" % (e if n>14 else sum(1/factorial[i] for i in range(n+1))))

if __name__ == "__main__":
    main()
