def base_to_int(code, lang):
    l = len(lang)
    s = 0
    n = 0
    m = {lang[i]: i for i in range(l)}
    for i in reversed(code):
        s += m[i] * l ** n
        n += 1
    return s


def int_to_base(num, lang):
    lst = []
    l = len(lang)
    m = {i: lang[i] for i in range(l)}
    while num > 0:
        lst = [m[num % l]] + lst
        num //= l
    return "".join(lst)


for j in range(int(input())):
    print('Case #{0}: {1}'.format(j+1, (lambda s: int_to_base(base_to_int(s[0], s[1]), s[2]))(input().split())))
