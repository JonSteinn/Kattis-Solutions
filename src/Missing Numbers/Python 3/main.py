helped = False
n = int(input())
next = 1
for i in range(n):
    x = int(input())
    for j in range(next, x):
        print(j)
        helped = True
    next = x + 1

if not helped:
    print('good job')