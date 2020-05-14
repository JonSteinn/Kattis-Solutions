def main():
    r,b = map(int,input().split())
    rb,f = r+b, 2
    while True:
        d,m = divmod(rb,f)
        if m == 0:
            if r == 2*d + 2*f - 4:
                print(d,f)
                break
        f += 1

if __name__ == "__main__":
    main()