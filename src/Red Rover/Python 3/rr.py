def all_substr(string):
    s = set()
    length = len(string)
    for i in range(length):
        for j in range(i, length + 1):
            s.add(string[i:j])
    return s


def compr(string, substring):
    l = len(substring)
    c = string.count(substring)
    return len(string) - c * (l-1) + l


def min_enc(string):
    x = len(string)
    for s in all_substr(string):
        y = compr(string, s)
        if y < x:
            x = y
    return x


print(min_enc(input()))