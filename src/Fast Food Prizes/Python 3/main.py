def claimed(cost, stickers):
    s = 0
    for r,p in cost:
        s += p*min(stickers[i-1] for i in r)
    return s

def main():
    for _ in range(int(input())):
        cost = []
        n,_ = map(int, input().split())
        for _ in range(n):
            cost.append((lambda l: (l[1:-1], l[-1]))(list(map(int, input().split()))))
        stickers = list(map(int,input().split()))
        print(claimed(cost, stickers))
        
if __name__ == "__main__":
    main()