from math import sqrt

def find(d):
    for i in range(1,int(sqrt(d))):
        numerator, denominator = d-i**2,i*2
        if numerator % denominator:
            continue
        x = numerator // denominator
        if (x + i)**2 - x**2 == d:
            return f'{x} {x+i}'
    return 'impossible'

def main():
    d = int(input())
    print(find(d))

if __name__ == "__main__":
    main()