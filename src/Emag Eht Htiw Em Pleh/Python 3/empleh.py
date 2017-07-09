filler = "+---+---+---+---+---+---+---+---+"
table = [
    [list("..."), list(":::"), list("..."), list(":::"), list("..."), list(":::"), list("..."), list(":::")],
    [list(":::"), list("..."), list(":::"), list("..."), list(":::"), list("..."), list(":::"), list("...")],
    [list("..."), list(":::"), list("..."), list(":::"), list("..."), list(":::"), list("..."), list(":::")],
    [list(":::"), list("..."), list(":::"), list("..."), list(":::"), list("..."), list(":::"), list("...")],
    [list("..."), list(":::"), list("..."), list(":::"), list("..."), list(":::"), list("..."), list(":::")],
    [list(":::"), list("..."), list(":::"), list("..."), list(":::"), list("..."), list(":::"), list("...")],
    [list("..."), list(":::"), list("..."), list(":::"), list("..."), list(":::"), list("..."), list(":::")],
    [list(":::"), list("..."), list(":::"), list("..."), list(":::"), list("..."), list(":::"), list("...")],
]

white = {'K': [], 'Q': [], 'R': [], 'B': [], 'N': [], 'P': []}
black = {'k': [], 'q': [], 'r': [], 'b': [], 'n': [], 'p': []}

_w = input().split()
if len(_w) > 1:
    for w in _w[1].split(','):
        if len(w) == 2:
            k = 'P'
            x, y = tuple(w)
            white[k].append((ord(x) - ord('a'), 8 - int(y)))
        else:
            k, x, y = tuple(w)
            white[k].append((ord(x) - ord('a'), 8 - int(y)))

_b = input().split()
if len(_b) > 1:
    for b in _b[1].split(','):
        if len(b) == 2:
            k = 'p'
            x, y = tuple(b)
            black[k.lower()].append((ord(x) - ord('a'), 8 - int(y)))
        else:
            k, x, y = tuple(b)
            black[k.lower()].append((ord(x) - ord('a'), 8 - int(y)))

for k, v in white.items():
    for a, b in v:
        table[b][a][1] = k

for k, v in black.items():
    for a, b in v:
        table[b][a][1] = k

print(filler)
for row in table:
    print("|" + "|".join(map(lambda s: "".join(s), row)) + "|")
    print(filler)