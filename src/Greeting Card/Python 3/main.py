class Points:
    STEPS = [
        (-2018,0),
        (-1680,-1118),
        (-1680,1118),
        (-1118,-1680),
        (-1118,1680),
        (0,-2018),
        (0,2018),
        (1118,-1680),
        (1118,1680),
        (1680,-1118),
        (1680,1118),
        (2018,0)
    ]

    def __init__(self):
        self.counter = 0
        self.points = set()

    def add(self, x, y):
        for a,b in Points.STEPS:
            if (x+a,y+b) in self.points:
                self.counter += 1
        self.points.add((x,y))

    def connections(self):
        return self.counter


def main():
    p = Points()
    for _ in range(int(input())):
        p.add(*map(int,input().split()))
    print(p.connections())

if __name__ == "__main__":
    main()

"""BRUTEFORCE search for integer points with valid distance

DIST_SQ = 4072324
for x in range(-2018,2018+1):
    for y in range(-2018,2018+1):
        if x**2 + y**2 == DIST_SQ:
            print(x,y)

Yields:
-2018 0
-1680 -1118
-1680 1118
-1118 -1680
-1118 1680
0 -2018
0 2018
1118 -1680
1118 1680
1680 -1118
1680 1118
2018 0
"""

