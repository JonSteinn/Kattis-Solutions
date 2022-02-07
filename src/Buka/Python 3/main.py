def main():
    a = int(input())
    op = input()
    b = int(input())
    print(a * b if op == "*" else a + b)

if __name__ == "__main__":
    main()
