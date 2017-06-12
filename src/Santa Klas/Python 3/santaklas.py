import math
print((lambda t: "safe" if t[1] <= 180 else int(t[0] / math.cos(math.pi * (t[1] / 180 + 0.5))))(tuple(map(lambda x: int(x), input().split()))))