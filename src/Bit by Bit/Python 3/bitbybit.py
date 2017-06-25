from collections import defaultdict


def true(c):
    return c == '1'


def false(c):
    return c == '0'


def _clear(i, b):
    b[i[0]] = '0'


def _set(i, b):
    b[i[0]] = '1'


def _or(i, b):
    if true(b[i[0]]) or true(b[i[1]]):
        b[i[0]] = '1'
    elif false(b[i[0]]) and false(b[i[1]]):
        b[i[0]] = '0'
    else:
        del b[i[0]]


def _and(i, b):
    if true(b[i[0]]) and true(b[i[1]]):
        b[i[0]] = '1'
    elif false(b[i[0]]) or false(b[i[1]]):
        b[i[0]] = '0'
    else:
        del b[i[0]]


commands = {"CLEAR": _clear, 'SET': _set, 'OR': _or, 'AND': _and}

while True:
    n = int(input())
    if n == 0:
        break
    bits = defaultdict(lambda: '?')
    for i in range(n):
        s = input().split()
        commands[s[0]](list(map(lambda z: int(z), s[1:])), bits)
    print("".join([bits[x] for x in reversed(range(32))]))

