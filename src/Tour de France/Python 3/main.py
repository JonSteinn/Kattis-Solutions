def max_spread(fs,rs):
    dr = sorted(n/m for m in fs for n in rs)
    return max(d2/d1 for d1,d2 in zip(dr,dr[1:]))

def main():
    while input() != '0':
        print('%.2f' % max_spread(
            list(map(int,input().split())), 
            list(map(int,input().split()))
        ))

if __name__ == "__main__":
    main()