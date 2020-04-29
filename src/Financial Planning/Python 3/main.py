def main():
    n,m = map(int,input().split())
    lis = sorted(((lambda a,b: (a,b,b//a+1))(*map(int,input().split())) for _ in range(n)),key=lambda z: (z[2],z[0],-z[1]))

    daily_profit = 0
    cost = 0
    days_needed = -1
    _next = 0
    day = lis[0][2]

    while True:
        while _next < len(lis) and lis[_next][2] == day:
            d,c,_ = lis[_next]
            cost += c
            daily_profit += d
            _next += 1

        if day*daily_profit - cost >= m:
            break
        day += 1
    print(day)

if __name__ == "__main__":
    main()