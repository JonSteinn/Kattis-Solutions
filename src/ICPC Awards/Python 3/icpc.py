won = set()
counter = 0
lis = []
for i in range(int(input())):
    s = input()
    if counter == 12:
        continue
    a, b = tuple(s.split())
    if a not in won:
        lis.append(s)
        won.add(a)
        counter += 1
print('\n'.join(lis))