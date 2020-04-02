from collections import defaultdict

def main():
    d1,d2 = defaultdict(lambda: 0), defaultdict(lambda: 0)
    _,w1,w2 = input().split()
    r,s = 0,0
    for a,b in zip(w1,w2):
        if a == b:
            r += 1
        else:
            d1[a] += 1
            d2[b] += 1
    for k in d1:
        if k in d2:
            s += min(d1[k],d2[k])
    print(r,s)

if __name__ == "__main__":
    main()