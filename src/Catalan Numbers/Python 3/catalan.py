catalan_dict = {0: 1, 1: 1}


def catalan(n):
    if catalan_dict.__contains__(n):
        return catalan_dict[n]
    if n <= 500:  # Max(ish) stack
        catalan_dict[n] = ((n << 2) - 2) * catalan(n-1) // (n + 1)
    else:
        catalan(n-500)
        catalan_dict[n] = ((n << 2) - 2) * catalan(n-1) // (n + 1)
    return catalan_dict[n]


for i in range(0, int(input())):
    print(catalan(int(input())))
