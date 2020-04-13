
def main():
    n,s,r = map(int,input().split())
    missing = set(map(int,input().split()))
    reserve = set(map(int,input().split()))
    for i in range(1,n+1):
        if i in missing:
            if i > 1 and i-1 in reserve:
                reserve.remove(i-1)
                missing.remove(i)
            elif i < n and i+1 in reserve:
                reserve.remove(i+1)
                missing.remove(i)
    print(len(missing))

if __name__ == "__main__":
    main()