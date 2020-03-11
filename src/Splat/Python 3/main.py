from math import pi

class Circle:
    def __init__(self,x,y,a,color):
        self.x = x
        self.y = y
        self.r_sq = a/pi
        self.color = color
    def __contains__(self, t):
        return (self.x-t[0])**2 + (self.y-t[1])**2 <= self.r_sq

def find_first(drops, x, y):
    for p in drops:
        if (x,y) in p:
            return p.color
    return 'white'

def test_case(drops, queries):
    for _ in range(queries):
        print(find_first(drops, *map(float, input().split())))

def main():
    for _ in range(int(input())):
        drops = list(reversed([Circle(
                *(lambda a,b,c,d: (float(a),float(b),float(c),d))(*input().split())) for _ in range(int(input())
        )]))
        queries = int(input())
        test_case(drops, queries)

if __name__ == "__main__":
    main()