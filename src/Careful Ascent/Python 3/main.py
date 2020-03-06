a,b = tuple(map(int, input().split()))
n = int(input())
shields = [(lambda r1, r2, r3: (int(r1), int(r2), float(r3)))(*input().split()) for _ in range(n)]
shields.append((b,))
s = shields[0][0]
for i in range(n):
    s += (shields[i][1]-shields[i][0])*shields[i][2]
    s += shields[i+1][0]-shields[i][1]
print('%.6f' % (a / s))