from sys import stdin
from heapq import heappop, heappush
from collections import Counter

def main():
    heap = []
    counter = Counter()
    total = 0

    for line in stdin:
        tree = line[:-1]
        if tree not in counter:
            heappush(heap, tree)
        counter[tree] += 1
        total += 1

    while heap:
        tree = heappop(heap)
        print('%s %.4f' % (tree, 100*counter[tree]/total))

if __name__ == "__main__":
    main()