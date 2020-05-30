def main():
    lis = sorted(int(input()) for _ in range(int(input())))
    h = 0
    while lis and lis[-1] > h:
        h += 1
        lis.pop()
    print(h)

if __name__ == "__main__":
    main()