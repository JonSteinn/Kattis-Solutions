table = []
for i in range(8):
    input()
    table += [list(map(lambda x: x[1:-1], input().split('|')[1:-1]))]
input()
table.reverse()

pieces = {'K': [], 'Q': [], 'R': [], 'B': [], 'N': [], 'P': [], 'k': [], 'q': [], 'r': [], 'b': [], 'n': [], 'p': []}

for i in range(8):
    for j in range(8):
        if table[i][j] in pieces.keys():
            pieces[table[i][j]] += [((lambda c: c.upper() if c.lower() != 'p' else '')(table[i][j]), chr(97+j), i + 1)]

for key, val in pieces.items():
    if key.isupper():
        val.sort(key=lambda x: (x[2], x[1]))
    else:
        val.sort(key=lambda x: (-x[2], x[1]))

print('White: ', end='')
print(','.join(list(map(lambda x: (x[0]+x[1]+str(x[2])), (pieces['K'] + pieces['Q'] + pieces['R'] + pieces['B'] + pieces['N'] + pieces['P'])))))
print('Black: ', end='')
print(','.join(list(map(lambda x: (x[0]+x[1]+str(x[2])), (pieces['k'] + pieces['q'] + pieces['r'] + pieces['b'] + pieces['n'] + pieces['p'])))))