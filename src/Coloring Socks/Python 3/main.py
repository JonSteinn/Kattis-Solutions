
def machines_needed(socks,cap,diff,colors):
    if colors[0]-colors[-1] <= diff and cap >= socks:
        return 1
    machines,curr_cap,i,j = (0,cap,0,0)
    while True:
        if curr_cap == 0:
            machines += 1
            curr_cap = cap
            i = j
        elif colors[i]-colors[j] > diff:
            machines += 1
            i = j
            curr_cap = cap
        elif j < socks-1:
            j += 1
            curr_cap -= 1
        else:
            return machines + 1


def main():
    s,c,k = map(int,input().split())
    colors = sorted(map(int,input().split()),reverse=True)
    print(machines_needed(s,c,k,colors))


if __name__ == "__main__":
    main()
