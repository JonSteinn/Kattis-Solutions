def main():
    n = int(input())
    lis = [(i,int(input())) for i in range(n)]
    best_start = sorted(lis, key=lambda z: z[1]+lis[(n + z[0] - 2) % n][1])[0][0]
    print(lis[best_start][1] + lis[(n + best_start - 2) % n][1])

if __name__ == "__main__":
    main()