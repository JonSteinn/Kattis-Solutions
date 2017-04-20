def first_collatz(n, visited):
    counter = 0
    while n > 1:
        counter += 1
        n = 3 * n + 1 if n & 1 else n >> 1
        if n not in visited:
            visited[n] = counter


def secondd_collatz(n, other):
    counter = 0
    if n not in other:
        while n > 1:
            counter += 1
            n = 3 * n + 1 if n & 1 else n >> 1
            if n in other:
                return n, counter
    return n, counter

while True:
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    if a == 0 or b == 0:
        break
    visitedA = {a: 0}
    first_collatz(a, visitedA)
    nc = secondd_collatz(b, visitedA)
    n = nc[0]
    c = nc[1]
    print("{:d} needs {:d} steps, {:d} needs {:d} steps, they meet at {:d}".format(a, visitedA[n], b, c, n))