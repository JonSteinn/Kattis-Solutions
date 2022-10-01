s, n = 0, 0
for val in map(ord, input()):
    s += val
    n += 1
print(chr(s//n))
