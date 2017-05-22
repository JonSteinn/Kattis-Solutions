import sys

for line in sys.stdin:
    print(sum(map(lambda x: int(x), line.split(' '))) // 2)