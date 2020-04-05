from collections import defaultdict
from operator import mul
from functools import reduce

def main():
    for _ in range(int(input())):
        disguises = defaultdict(lambda: 1)
        for _ in range(int(input())):
            _,b = input().split()
            disguises[b] += 1
        print(reduce(mul, disguises.values(), 1) - 1)

if __name__ == "__main__":
    main()