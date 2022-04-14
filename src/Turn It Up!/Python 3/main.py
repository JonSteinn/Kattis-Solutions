n = 7
for _ in range(int(input())):
    n = min(10, max(0, n + (1 if input()[-2] == 'p' else -1)))
print(n)