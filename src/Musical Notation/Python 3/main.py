mat = [
    list('G: '),
    list('F: '),
    list('E: '),
    list('D: '),
    list('C: '),
    list('B: '),
    list('A: '),
    list('g: '),
    list('f: '),
    list('e: '),
    list('d: '),
    list('c: '),
    list('b: '),
    list('a: ')
]
indices = {
    'G': 0,
    'F': 1,
    'E': 2,
    'D': 3,
    'C': 4,
    'B': 5,
    'A': 6,
    'g': 7,
    'f': 8,
    'e': 9,
    'd': 10,
    'c': 11,
    'b': 12,
    'a': 13
}
hyph = {'F', 'D', 'B', 'g', 'e', 'a'}


def main():
    n = int(input())
    n = n + n - 1
    replacements = []
    for c in input().split():
        if len(c) > 1:
            t = int(c[1:])
            n += t - 1
            replacements.extend([c[0]] * t)
        else:
            replacements.append(c)
        replacements.append('!')
    replacements.pop()
    for x in mat:
        if x[0] in hyph:
            x.extend(['-']*n)
        else:
            x.extend([' ']*n)
    for i,r in enumerate(replacements):
        if r != '!':
            mat[indices[r]][3 + i] = '*'
    print('\n'.join(''.join(x) for x in mat))

if __name__ == "__main__":
    main()