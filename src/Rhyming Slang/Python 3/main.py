def main():
    common,rhymes = input(),set()
    for _ in range(int(input())):
        inp = input().split()
        if any(common.endswith(x) for x in inp):
            rhymes.update(inp)
    for _ in range(int(input())):
        w = input().split()[-1]
        print('YES' if any(w.endswith(x) for x in rhymes) else 'NO')

if __name__ == "__main__":
    main()