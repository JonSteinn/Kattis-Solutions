import sys
from itertools import starmap


print('\n'.join(starmap(lambda h,t: (lambda c: str(c + (t+c)//2 + (h + (t+c)//2)//2))(((h % 2) * 2 + (t % 4) * 3) % 4), (tuple(map(int, z.split())) for z in sys.stdin.readlines()[:-1]))))
