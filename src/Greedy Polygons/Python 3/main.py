from math import pi, tan

def cot(x):
    return 1/tan(x)

def angle_expansion(d,g):
    # The interior angle of an angle is (n-2)/n * pi. Take two adjacent
    # sides, their normals for the angle for which the expansion is circular.
    # The normals form two pi/2 angles with the sides so the angle between them
    # must be
    #   2*pi - pi/2 - pi/2 - (n-2)/n * pi = pi - (n-2)/n * pi 
    # = pi*(1-(n-2)/n) = pi*((n-(n-2))/n) = pi*(2/n) = 2*pi / n
    # 
    # The radius is g*d and we have (2*pi/n) / (2*pi) = 1/n parts of the circle.
    # There are n such parts so we have n*1/n * (g*d)**2 * pi = (g*d)**2 * pi
    return (g*d)**2 * pi

def side_expansion(n,l,d,g):
    # n sides (=> n squares)
    # Each square has length l and width d*g
    return n*l*d*g

def ngon_area(n,l):
    # Formula: https://en.wikipedia.org/wiki/Regular_polygon
    return 0.25 * n * l**2 * cot(pi / n)

def expanded_area(n,l,d,g):
    return ngon_area(n,l) + side_expansion(n,l,d,g) + angle_expansion(d,g)

def main():
    for _ in range(int(input())):
        n,l,d,g = map(int,input().split())
        print('%.6f' % expanded_area(n,l,d,g))

if __name__ == "__main__":
    main()