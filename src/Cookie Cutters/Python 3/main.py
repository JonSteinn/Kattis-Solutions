from math import sqrt

# Shoelace formula
def area(pnts):
    return abs(sum(pnts[i][0]*pnts[i+1][1]-pnts[i+1][0]*pnts[i][1] for i in range(len(pnts)-1)) + pnts[-1][0]*pnts[0][1] - pnts[0][0]*pnts[-1][1])/2

def main():
    pnts = [tuple(map(float,input().split())) for _ in range(int(input()))]
    scale = sqrt(int(input()) / area(pnts))
    xs,ys,o_x,o_y = [],[],0,0
    for x,y in pnts:
        xs.append(x*scale)
        ys.append(y*scale)
        o_x = min(o_x, xs[-1])
        o_y = min(o_y, ys[-1])
    for x,y in zip(xs,ys):
        print('%.4f %.4f' % (x - o_x, y - o_y))

if __name__ == "__main__":
    main()