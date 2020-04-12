def rooms(lis):
    counter = 0
    while lis:
        counter += 1
        a,b = lis.pop()
        while lis and (a <= lis[-1][0] <= b or a <= lis[-1][1] <= b):
            _a,_b = lis.pop()
            a = max(a,_a)
            b = min(b,_b)
    return counter

def main():
    n = int(input())
    lis=sorted((tuple(map(int,input().split())) for _ in range(n)),reverse=True)
    print(rooms(lis))

if __name__ == "__main__":
    main()