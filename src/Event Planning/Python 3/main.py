from heapq import heappush, heappop

def find_minimum(prices, b, n):
    while prices:
        money_needed = n*heappop(prices)
        if money_needed <= b:
            return money_needed
    return 'stay home'

def main():
    n,b,h,_ = map(int, input().split())
    prices = []
    for _ in range(h):
        price = int(input())
        if any(x >= n for x in map(int, input().split())):
            heappush(prices, price)
    print(find_minimum(prices, b, n))

if __name__ == "__main__":
    main()