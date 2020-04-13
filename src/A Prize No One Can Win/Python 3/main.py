def main():
    n,x = map(int,input().split())
    items = sorted(map(int,input().split()))
    if n == 1:
        print('1')
    elif items[-1] + items[-2] <= x:
        print(n)
    else:
        for i,c in enumerate(items):
            if c + items[i+1] > x:
                print(i+1)
                break

if __name__ == "__main__":
    main()