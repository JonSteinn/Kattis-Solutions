import sys


def next_digit(lst):
    if lst[0] < lst[1]:
        lst[0] *= 10
        n = lst[0] // lst[1]
        lst[0] -= n * lst[1]
        return str(n)
    else:
        lst[0] -= lst[1]
        return '1'


def sequence(line):
    lis = list(map(lambda x: int(x), line.split()))
    return ''.join(['0', '.'] + [next_digit(lis) for i in range(lis[2])])


for _line in sys.stdin:
    print(sequence(_line))