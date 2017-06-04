def test_case(dom, cod):
    n = int(input())
    dic = {}
    for i in range(0, n):
        f = input().split(' -> ')
        dic[f[0]] = f[1]
    f_dom = set(dic.keys())
    f_cod = set(dic.values())
    if len(dic) != n or not f_dom.issubset(dom) or not f_cod.issubset(cod):
        return 'not a function'
    surjective = cod == f_cod
    injective = len(dic.values()) == len(f_cod)
    if surjective:
        if injective:
            return 'bijective'
        else:
            return 'surjective'
    else:
        if injective:
            return 'injective'
        else:
            return 'neither injective nor surjective'

while True:
    try:
        dom = set(input().split()[1:])
        cod = set(input().split()[1:])
        print(test_case(dom, cod))
    except EOFError:
        break