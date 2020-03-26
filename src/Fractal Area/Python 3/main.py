from math import pi

def fractal_area(r,n):
    first = r**2
    if n == 1:
        return first * pi
    second = 4 * (r/2)**2
    if n == 2:
        return (first + second) * pi
    rest = sum((r/2**i)**2 * 4*3**(i-1) for i in range(2,n))
    return (first + second + rest) * pi

def main():
    for _ in range(int(input())):
        r,n = map(int, input().split())
        print('%.6f' % fractal_area(r,n))

if __name__ == "__main__":
    main()