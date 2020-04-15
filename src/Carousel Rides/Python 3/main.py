INF = 2147483647

def test_case(prices,m):
    a,b = (1,INF)
    for _a,_b in prices:
        if _a <= m and (_b/_a < b/a or (_b/_a == b/a and _a > a)):
            a,b = _a,_b

    if b != INF:
        print(f'Buy {a} tickets for ${b}')
    else:
        print('No suitable tickets offered')

def main():
    while True:
        n,m = map(int,input().split())
        if n+m == 0:
            break
        gen = (map(int,input().split()) for _ in range(n))
        test_case(gen,m)

if __name__ == "__main__":
    main()