import itertools


def is_square_free(n: int) -> bool:
    i = 2
    while i * i <= n:
        occ = 0
        while n % i == 0:
            n = n // i
            occ += 1
            if occ > 1:
                return False
        i = i + 1
    return True


k = int(input())
for i in itertools.chain((2, 3), range(5, k, 2)):
    if is_square_free(i * k):
        print(i)
        break
