def compositions(n,m,k,mem):
    if (n,m,k) not in mem:
        if n==0:
            return 1
        s = 0
        for i in range(n,0,-1):
            if i % k != m:
                s += compositions(n-i,m,k,mem)
        mem[(n,m,k)] = s
    return mem[(n,m,k)]

def main():
    mem = {}
    for _ in range(int(input())):
        case, n, m, k = map(int,input().split())
        print(f'{case} {compositions(n,m,k,mem)}')

if __name__ == "__main__":
    main()