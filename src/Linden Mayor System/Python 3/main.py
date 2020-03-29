def main(getline = input):
    n,m = map(int, getline().split())
    rules = [chr(65+i) for i in range(26)]
    for _ in range(n):
        a,b = getline().split(' -> ')
        rules[ord(a) - 65] = b
    curr = getline()
    for _ in range(m):
        curr = ''.join((rules[ord(c) - 65] for c in curr))
    print(curr)

if __name__ == "__main__":
    main()