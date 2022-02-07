def main():
    first = None
    for _ in range(int(input())):    
        nxt = int(input())
        if first is None:
            first = nxt
        elif nxt % first == 0:
            print(nxt)
            first = None

if __name__ == "__main__":
    main()
