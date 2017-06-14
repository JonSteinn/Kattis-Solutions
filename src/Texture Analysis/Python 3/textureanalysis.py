n = 1
while True:
    s = input()
    if s == 'END':
        break
    if len(s) == 1 or len(set((lambda z: [z[i + 1] - z[i] for i in range(len(z)-1)])(list(map(lambda y: y[0], (filter(lambda x: x[1] == '*', enumerate(list(s))))))))) == 1:
        print(n, 'EVEN')
    else:
        print(n, 'NOT EVEN')
    n += 1