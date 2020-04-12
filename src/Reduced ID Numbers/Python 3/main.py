def main():
    n = int(input())
    ids = list(int(input()) for _ in range(n))
    if n == 1:
        print(1)
    else:
        i = 2
        while True:
            if len(set(x % i for x in ids)) == n:
                print(i)
                break
            i += 1

if __name__ == "__main__":
    main()