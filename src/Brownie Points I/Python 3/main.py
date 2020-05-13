def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        score = [0]*3
        pnts = [tuple(map(int,input().split())) for _ in range(n)]
        x_o,y_o = pnts[len(pnts)//2]
        for a,b in pnts:
            # Could save half of this iteration by doing it as you 
            # read 2nd half, but not to bothered... 
            score[sign((a-x_o)*(b-y_o))] += 1
        print(*score[1:])

if __name__ == "__main__":
    main()