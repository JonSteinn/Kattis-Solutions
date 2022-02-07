def main():
    n, m = map(int, input().split())
    left = 0
    for grp in map(int, input().split()):
        if grp > n:
            left += 1
        else:
            n -= grp
    print(left)

if __name__ == "__main__":
    main()
