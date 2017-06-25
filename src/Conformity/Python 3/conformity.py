from collections import defaultdict

d = defaultdict(lambda: 0)
for i in range(int(input())):
    d[tuple(sorted(input().split()))] += 1

lst = sorted(list(d.values()), reverse=True)
most = lst[0]
run = 1
for i in lst[1:]:
    if i == most:
        run += 1
    else:
        break
print(run * most)