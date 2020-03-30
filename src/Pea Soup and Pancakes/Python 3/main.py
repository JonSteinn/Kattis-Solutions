def main():
    for _ in range(int(input())):
        menu_items = int(input())
        name = input()
        s = {'pancakes','pea soup'}
        for _ in range(menu_items):
            s.discard(input())
            if not s:
                print(name)
                return
    print('Anywhere is fine I guess')

if __name__ == "__main__":
    main()