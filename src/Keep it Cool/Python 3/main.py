def optimal(n,m,s,d,slots):
    index,placement = 0,[0]*s
    for i,f in slots:
        if n == 0 or d == f:
            break
        placement[i] = min(n,d-f)
        n -= placement[i]
        index += 1
    if sum(z[1] for z in slots[index:]) < m:
        return ('impossible',)
    return placement

def main():
    print(*optimal(*map(int, input().split()),sorted(enumerate(map(int,input().split())),key=lambda z: z[1])))

if __name__ == "__main__":
    main()
