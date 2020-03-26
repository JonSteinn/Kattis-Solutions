from collections import deque
from itertools import combinations

def generate_all(original, pairs):
    n = len(pairs)
    collect = set()
    for i in range(1,n+1):
        for r in combinations(pairs, i):
            remove = {ind for pair in r for ind in pair}
            collect.add(''.join(c for i,c in enumerate(original) if i not in remove))
    return sorted(collect)

def main():
    stack = deque()
    pairs = []
    original = input()
    for i,x in enumerate(original):
        if x == '(':
            stack.append(i)
        elif x == ')':
            pairs.append((stack.pop(), i))
    print('\n'.join(generate_all(original, pairs)))

if __name__ == "__main__":
    main()