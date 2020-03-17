from math import sqrt, acos, pi

def length(r,h,s):
    straight_part = 2*sqrt(h**2-r**2)
    angle_to_straight_part = pi/2 - acos(r/h)
    circular_part = 2*pi*r * (pi + angle_to_straight_part*2)/(2*pi)
    return (straight_part+circular_part)*(1+s/100)

def main():
    while True:
        r,h,s = map(int, input().split())
        if r+h+s == 0:
            break
        print('%.2f' % length(r,h,s))

if __name__ == "__main__":
    main()