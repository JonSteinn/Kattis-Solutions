parts = set()
p, n = tuple(map(int, input().split()))
for i in range(n):
    parts.add(input())
    if len(parts) == p:
        print(i + 1)
        break
else:
    print('paradox avoided')