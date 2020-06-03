def min_max(w,g,h,_r):
    line = (w**2 + (g-h)**2)**0.5
    cost = lambda x: (x**2 + (g-_r)**2)**0.5 + ((w-x)**2 + (h-_r)**2)**0.5
    l,r = 0,w
    while True:
        if abs(r - l) < 0.000001:
            return line, cost((l + r) / 2)
        c1, c2 = l + (r - l) / 3, r - (r - l) / 3
        if cost(c1) < cost(c2):
            r = c2
        else:
            l = c1

def main():
    for _ in range(int(input())):
        print(*min_max(*map(int,input().split())))

if __name__ == "__main__":
    main()