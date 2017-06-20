v = ['aa', 'ee', 'ii', 'oo', 'uu', 'yy']
while True:
    n = int(input())
    if n == 0:
        break
    most = -1
    li = []
    for i in range(n):
        s = input()
        val = sum([s.count(x) for x in v])
        if val > most:
            most = val
            li = [s] + li
    print(li[0])