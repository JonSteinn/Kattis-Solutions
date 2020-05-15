import sys

def dist_squared(x,y,a,b):
    return (x-a)**2 + (y-b)**2

def main():
    for i, line in enumerate(sys.stdin):
        if not i:
            g_x, g_y, d_x, d_y = map(float,line.split())
        else:
            x,y = map(float,line.split())
            if 4*dist_squared(g_x,g_y,x,y) < dist_squared(d_x,d_y,x,y):
                print('The gopher can escape through the hole at (%.3f,%.3f).' % (x,y))
                return
    print('The gopher cannot escape.')

if __name__ == "__main__":
    main()