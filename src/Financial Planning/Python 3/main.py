def main():
    # Read the input values n and m
    n, m = map(int, input().split())
    
    # Create a list of tuples containing information for each day: (d, c, days_needed)
    # d: daily profit, c: cost, days_needed: days needed to complete the task
    lis = sorted(
        (
            (
                lambda a, b: (a, b, b // a + 1)
            )(*map(int, input().split()))
            for _ in range(n)
        ),
        key=lambda z: (z[2], z[0], -z[1])
    )

    daily_profit = 0
    cost = 0
    days_needed = -1
    _next = 0
    day = lis[0][2]

    while True:
        # Calculate the total daily profit and cost for the current day
        while _next < len(lis) and lis[_next][2] == day:
            d, c, _ = lis[_next]
            cost += c
            daily_profit += d
            _next += 1

        # Check if the accumulated profit is enough to cover the target profit m
        if day * daily_profit - cost >= m:
            break
        
        day += 1  # Increment the day
    print(day)  # Print the final day needed to achieve the target profit

if __name__ == "__main__":
    main()
