def main():
    n = int(input())
    ids = list(int(input()) for _ in range(n))
    while True:
        if len(set(x % n for x in ids)) == len(ids):
            print(n)
            break
        n += 1

if __name__ == "__main__":
    main()