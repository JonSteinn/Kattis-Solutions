lis = [int(input())]
while lis[-1] != 1:
    lis.append(lis[-1] * 3 + 1 if lis[-1] & 1 else lis[-1] // 2)
print(len(lis))