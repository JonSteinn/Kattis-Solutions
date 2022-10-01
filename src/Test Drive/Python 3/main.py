def action(d1: int, d2: int) -> str:
    if d1 * d2 < 0:
        return "turned"
    elif abs(d1) < abs(d2):
        return "accelerated"
    elif abs(d1) > abs(d2):
        return "braked"
    else:
        return "cruised"

a,b,c = map(int, input().split())
print(action(b - a, c - b))