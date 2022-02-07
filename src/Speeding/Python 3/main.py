t1, d1, t2, d2, b = (0,) * 5
for _ in range([int(input()), input()][0] - 1):
    t2, d2 = map(int, input().split())
    b = max(b, (d2-d1) // (t2-t1))
    t1, d1 = t2, d2
print(b)