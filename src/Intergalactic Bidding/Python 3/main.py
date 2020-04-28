def main():
    n,s = map(int,input().split())
    wins = []
    for x,name in sorted(((lambda a,b:(int(b),a))(*input().split()) for _ in range(n)), reverse=True):
        if s >= x:
            wins.append(name)
            s -= x
    print('0' if s else (lambda a,b: f'{a}\n{b}')(*(lambda w: (len(w),'\n'.join(w)))(wins)))

if __name__ == "__main__":
    main()