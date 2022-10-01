n, cap = map(int, input().split())
curr, refill = cap, 0
for _ in range(n):
    x = input()
    if x.endswith("L"):
        x = int(x[:-1]) + 1
    else:
        x = int(x)
    if curr - x < 0:
        refill += 1
        curr = cap - x
    else:
        curr -= x
print(refill)