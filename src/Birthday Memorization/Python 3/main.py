from heapq import heappush as hpush, heappop as hpop
from collections import defaultdict as dd

def main():
    d = dd(list)
    for _ in range(int(input())):
        name, like, bday = input().split()
        hpush(d[bday], (-int(like), name))
    print(len(d))
    print("\n".join(sorted(map(lambda z: hpop(z)[1], d.values()))))

if __name__ == "__main__":
    main()
