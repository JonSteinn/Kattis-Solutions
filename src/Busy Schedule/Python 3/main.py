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

        for h, m, t in sorted(((lambda n,c: (*(lambda h,m: (h if h != 12 else -1, m))(*map(int, n.split(':'))),c[0]))(*input().split()) for _ in range(n)), key=lambda z: (z[2],z[0],z[1])):
            if h == -1:
                h = 12
            if m < 10:
                m = f'0{m}'
            t = 'a.m.' if t == 'a' else 'p.m.'
            print(f'{h}:{m} {t}')

if __name__ == "__main__":
    main()