n, m = map(int, input().split())
friends = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    friends[a - 1] += 1
    friends[b - 1] += 1
print(" ".join((str(cnt - i - 1) for i, cnt in enumerate(friends))))