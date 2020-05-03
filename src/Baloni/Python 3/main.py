from collections import defaultdict

def main():
    s = defaultdict(lambda: 0)
    input()
    total = 0
    for x in map(int, input().split()):
        if s[x+1] > 0:
            s[x+1] -= 1
        else:
            total += 1
        s[x] += 1
    print(total)

if __name__ == "__main__":
    main()