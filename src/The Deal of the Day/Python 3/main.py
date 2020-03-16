def ascending(cards,remaining):
    if remaining == 0:
        return 1
    if len(cards) < remaining:
        return 0
    if len(cards) == remaining:
        ways = 1
        for card in cards:
            ways *= card
        return ways
    return cards[0]*ascending(cards[1:], remaining-1) + ascending(cards[1:], remaining)

print(ascending(list(map(int,input().split())), int(input())))