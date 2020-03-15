from collections import Counter

print('\n'.join((lambda r,c: ''.join(map(lambda z: Counter(z).most_common(1)[0][0], zip(*[input() for _ in range(r)]))))(*map(int,input().split())) for _ in range(int(input()))))