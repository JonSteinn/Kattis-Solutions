def main():
    n,v = map(int,input().split())
    best = (lambda a,b,c: a*b*c - v)(*map(int,input().split()))
    for _ in range(n-1):
        curr = (lambda a,b,c: a*b*c - v)(*map(int,input().split()))
        if curr > best:
            best = curr
    print(best)

if __name__ == "__main__":
    main()