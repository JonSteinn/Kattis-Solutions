n = int(input().split()[0])
s = set(input().split())
for _ in range(n-1):
    s.intersection_update(input().split())
print(len(s))
print("\n".join(sorted(s)))