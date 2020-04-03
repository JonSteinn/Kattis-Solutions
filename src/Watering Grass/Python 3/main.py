import sys
from math import sqrt

def optimal(lis, l, n):
    assert(len(lis)==n)
    c,i,lo = (0,)*3
    while True:
        furthest = -1
        while i < n and lis[i][0] <= lo:
            furthest = max(furthest, lis[i][1])
            i += 1
        if furthest == -1:
            return -1
        c += 1
        lo = furthest
        if lo >= l:
            return c

def main():
    state = 0
    for line in sys.stdin:
        if state == 0:
            lis = []
            n,l,w = map(int,line.split())
            state = n
            half_w_square = (w/2)**2
        else:
            state -= 1
            x,r = map(int,line.split())
            if 2*r > w:
                d = sqrt(r**2 - half_w_square)
                lis.append((x-d,x+d))
            if state == 0:
                print(optimal(sorted(lis),l,len(lis)))

if __name__ == "__main__":
    main()