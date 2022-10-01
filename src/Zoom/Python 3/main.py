import itertools
print((lambda k: ' '.join(map(str, itertools.islice(map(int, input().split()), k - 1, None, k))))(int(input().split()[1])))