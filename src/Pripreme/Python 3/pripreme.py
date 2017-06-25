input()
s = 0
m = 0
for i in map(lambda z: int(z), input().split()):
    s += i
    m = max(m, i)
print(m*2 if m > s-m else s)
