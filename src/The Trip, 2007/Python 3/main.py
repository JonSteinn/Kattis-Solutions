from collections import defaultdict

def place_bags(bags,n):
    while n:
        rem = set()
        group = []
        for k,v in bags.items():
            if v:
                group.append(str(v.pop()))
                n -= 1
            if not v:
                rem.add(k)
        for k in rem:
            del bags[k]
        print(' '.join(group))

def test_case(n):
    k,bags,i = 0,defaultdict(list),0
    while i < n:
        for x in map(int,input().split()):
            i += 1
            bags[x].append(x)
            k = max(k, len(bags[x]))
    print(k)
    place_bags(bags,n)

def main():
    first = True
    while True:
        n = int(input())
        if n == 0:
            break
        if first:
            first = False
        else:
            print()
        test_case(n)

if __name__ == "__main__":
    main()