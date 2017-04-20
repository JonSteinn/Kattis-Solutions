def sum_ab(a, b):
    return b * (b+1) // 2 - a*(a-1)//2


def split_check(n, k):
    if (n & (n - 1)) == 0:
        return -1
    start = n//k - k//2
    end = start + k - 1
    if sum_ab(start, end) == n:
        return start
    if sum_ab(start+1, end+1) == n:
        return start + 1
    return 0


def find_sum(n):
    split = 2
    while True:
        start = split_check(n, split)
        if start != 0:
            break
        split += 1
    if start < 0:
        return "IMPOSSIBLE"
    return "{:d} = {:d}".format(n, start) + (" + {:d}" * (split - 1)).format(*[start + 1 + i for i in range(0, split - 1)])

for i in range(0, int(input())):
    print(find_sum(int(input())))