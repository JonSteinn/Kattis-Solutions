from collections import defaultdict

while True:
    n = int(input())
    if n == 0:
        break
    d = defaultdict(list)
    for i in range(n):
        s = input().split()
        for w in s[1:]:
            d[w].append(s[0])
    for k in sorted(d.keys()):
        print(k, " ".join(sorted(d[k])))
    print()