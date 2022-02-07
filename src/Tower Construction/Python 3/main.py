def main():
    last, cnt = 0, 0
    _ = input()
    for i in map(int, input().split()):
        if i > last:
            cnt += 1
        last = i
    print(cnt)

if __name__ == "__main__":
    main()