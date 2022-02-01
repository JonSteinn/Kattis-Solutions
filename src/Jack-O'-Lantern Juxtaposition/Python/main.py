from functools import reduce

print(reduce(lambda a, b: a * b, map(int, input().split()), 1))