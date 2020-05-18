def least_average(lis):
    total,time = 0,0
    for x in lis:
        time += x
        total += time
    return total / len(lis)

def main():
    for _ in range(int(input())):
        print('%.6f' % least_average(sorted(sum(map(int, input().split()[1:])) for _ in range(int(input())))))

if __name__ == "__main__":
    main()