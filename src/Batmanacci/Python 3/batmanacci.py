from collections import defaultdict

fibs = defaultdict(lambda: -1)
fibs[1] = 1
fibs[2] = 1


def length(n):
    if n > 87:
        return -1
    if n not in fibs:
        fibs[n] = length(n - 2) + length(n-1)
    return fibs[n]


def bat(n, k):
    if n == 1:
        return 'N'
    if n == 2:
        return 'A'
    l = length(n-2)
    while l == -1:
        n -= 1
        l = length(n-2)
    if l < k:
        return bat(n-1, k-l)
    return bat(n-2, k)


a, b = tuple(map(int, input().split()))
print(bat(a, b))