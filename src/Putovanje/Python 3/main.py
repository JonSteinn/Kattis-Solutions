def most_fruits(lis, n, c):
    longest_run = -1
    for i in range(n):
        t,j,r = c,i,0
        while j < n and t > 0:
            if lis[j] <= t:
                t -= lis[j]
                r += 1
            j += 1
        longest_run = max(longest_run, r)
    return longest_run    

def main():
    n,c = map(int,input().split())
    l = list(map(int,input().split()))
    print(most_fruits(l,n,c))

if __name__ == "__main__":
    main()