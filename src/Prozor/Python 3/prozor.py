r, s, k = tuple(map(int, input().split()))
flies = set()
for i in range(r):
    for j, c in enumerate(input()):
        if c == '*':
            flies.add((j, i))

best = ((), -1)
for i in range(r - k + 1):
    for j in range(s - k + 1):
        counter = 0
        for x, y in flies:
            if i < y < i + k - 1 and j < x < j + k - 1:
                counter += 1
        if counter > best[1]:
            best = ((j, i), counter)

print(best[1])
nw = best[0]
d = {
    nw: '+',
    (nw[0] + k - 1, nw[1]): '+',
    (nw[0], nw[1] + k - 1): '+',
    (nw[0] + k - 1, nw[1] + k - 1): '+',
}
for i in range(1, k - 1):
    d[(nw[0] + i, nw[1])] = '-'
    d[(nw[0] + i, nw[1] + k - 1)] = '-'
for i in range(1, k - 1):
    d[(nw[0], nw[1] + i)] = '|'
    d[(nw[0] + k - 1, nw[1] + i)] = '|'

for i in range(r):
    print(''.join([d[(j, i)] if (j, i) in d else ('*' if (j, i) in flies else '.') for j in range(s)]))