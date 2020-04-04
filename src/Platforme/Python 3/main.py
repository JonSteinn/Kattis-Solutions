def length(platforms):
    #O(n^2) is fine for n=100
    s=0
    for i,(y,x1,x2) in enumerate(platforms):
        l,r = -1,-1
        x2-=1
        for y2,x3,x4 in reversed(platforms[:i]):
            x4-=1
            if l == -1 and x3 <= x1 <= x4:
                l = y-y2
            if r == -1 and x3 <= x2 <= x4:
                r = y-y2
            if l != -1 and r != -1:
                break
        s += (l if l != -1 else y)+(r if r != -1 else y)
    return s

def main():
    print(length(sorted(tuple(map(int,input().split())) for _ in range(int(input())))))

if __name__ == "__main__":
    main()