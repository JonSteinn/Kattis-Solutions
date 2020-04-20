def main():
    p,t = map(int,input().split())
    opinions = [set() for _ in range(p)]
    try:
        for _ in range(p*t):
            _p,_t = map(int,input().split())
            opinions[_p-1].add(_t)
    except EOFError:
        pass
    print(len({frozenset(s) for s in opinions}))

if __name__ == "__main__":
    main()