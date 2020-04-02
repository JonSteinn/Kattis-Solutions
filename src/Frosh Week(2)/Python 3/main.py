
def main():
    i,j,(n,m) = 0,0,map(int,input().split())
    tasks = sorted(map(int,input().split()),reverse=True)
    intervals = sorted(map(int,input().split()),reverse=True)
    while i < n and j < m:
        if tasks[i] <= intervals[j]:
            i,j = i+1,j+1
        else:
            i = i+1
    print(j)

if __name__ == "__main__":
    main()