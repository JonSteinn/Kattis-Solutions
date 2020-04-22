def main():
    d = {}
    most = int(input())
    for i, l in enumerate(map(int,input().split())):
        if l not in d:
            d[l] = i
        else:
            most = min(most, i - d[l])
            d[l] = i
    print(most)

if __name__ == "__main__":
    main()