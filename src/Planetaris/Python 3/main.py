def wins(a, es):
    s = 0
    for i,x in es:
        if a > x:
            s += 1
            a -= (x+1)
        else:
            return i
    return i+1

def main():
    _,a = map(int,input().split())
    print(wins(a,enumerate(sorted(map(int,input().split())))))

if __name__ == "__main__":
    main()