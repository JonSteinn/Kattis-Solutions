n = int(input())
TB, LR = (0,)*2
for i in range(n):
    a, b = (lambda s: (s[:2].count('0'), s[2:].count('0')))(input())
    TB += a
    LR += b
swords = min(TB,LR) // 2
print(f'{swords} {TB - swords*2} {LR - swords*2}')