from operator import itemgetter

def main():
    last_end, cnt = -1, 0
    for a,b in sorted((tuple(map(int, input().split())) for _ in range(int(input()))), key=itemgetter(1)):
        if a >= last_end:
            last_end = b
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()
