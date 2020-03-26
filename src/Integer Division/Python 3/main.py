from collections import defaultdict

def main():
    c = defaultdict(lambda: 0)
    d = int(input().split()[1])
    for x in map(int,input().split()):
        c[x//d] += 1
    print(sum((x*(x-1))//2 for x in c.values()))

if __name__ == "__main__":
    main()