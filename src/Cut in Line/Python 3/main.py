def main():
    lis = [input() for _ in range(int(input()))]
    for _ in range(int(input())):
        cmd = input().split()
        if len(cmd) == 2:
            lis.remove(cmd[1])
        else:
            lis.insert(lis.index(cmd[2]), cmd[1])
    print("\n".join(lis))

if __name__ == "__main__":
    main()