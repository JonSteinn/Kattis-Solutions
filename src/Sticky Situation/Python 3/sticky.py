def valid(a, b, c):
    return a < b + c and b < a + c and c < a + b


input()
sides = sorted(list(map(lambda x: int(x), input().split())))
found = False
for i in range(len(sides) - 2):
    if valid(sides[i], sides[i + 1], sides[i + 2]):
        found = True
        break
if found:
    print('possible')
else:
    print('impossible')