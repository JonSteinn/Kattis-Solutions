def main():
    n = int(input())
    k = n % 4
    if k == 0:
        print('Even')
    elif k == 2:
        print('Odd')
    else:
        print('Either')

if __name__ == "__main__":
    main()