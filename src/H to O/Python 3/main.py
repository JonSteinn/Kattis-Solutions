from collections import Counter
import re

# Some convenience over performance, additional O(2500) doesn't relly matter
def add_ones(formula):
    lis = []
    for i,c in enumerate(formula):
        lis.append(c)
        if not c.isnumeric() and (i == len(formula) - 1 or not formula[i+1].isnumeric()):
            lis.append('1')
    return ''.join(lis)

def ingredients(formula):
    c = Counter()
    for a, b in re.findall(r"([A-Z]+)([0-9]+)", add_ones(formula)):
        c[a] += int(b)
    return c

def create_from(f1,f2,n):
    total = 2147483647
    for k,v in f2.items():
        total = min(total, (f1[k]*n) // v)
    return total

def main():
    (f1, n), f2 = input().split(), input()
    print(create_from(ingredients(f1), ingredients(f2), int(n)))

if __name__ == "__main__":
    main()