from functools import reduce
print((lambda init, seq: reduce(lambda p, c: (p[0] - c, p[1] + 1 if p[0]-c < 0 else p[1]), seq, init)[1])((next(map(int, input().split())), 0), map(int, input().split())))
