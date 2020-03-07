from collections import defaultdict

def test_case():
    n = int(input())
    counter = defaultdict(lambda: 0)
    for _ in range(n):
        a,b = tuple(input().split())
        counter[a] += int(b)
    print(len(counter))
    for k, v in sorted(counter.items(), key=lambda z: (-z[1],z[0])):
        print(f'{k} {v}')

def main():
    tc = int(input())
    for _ in range(tc):
        test_case()

if __name__ == "__main__":
    main()