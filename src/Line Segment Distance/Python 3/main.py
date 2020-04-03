from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_squared(self,other):
        return (self.x-other.x)**2 + (self.y-other.y)**2

class LineSegment:
    COLINEAR = 0
    CLOCKWISE = 1
    COUNTER_CLOCKWISE = 2

    def __init__(self, x1, y1, x2, y2):
        self.a = Point(x1,y1)
        self.b = Point(x2,y2)

    def length_squared(self):
        return (self.a.x-self.b.x)**2 + (self.a.y-self.b.y)**2

    def contains(self, point):
        return min(self.a.x, self.b.x) <= point.x <= max(self.a.x, self.b.x) \
            and min(self.a.y, self.b.y) <= point.y <= max(self.a.y, self.b.y)
    
    def orientation(self, point):
        val = (self.a.y - self.b.y) * (point.x - self.a.x) - (self.a.x - self.b.x) * (point.y - self.a.y)
        return 1 if val > 0 else (2 if val < 0 else 0)

    def intersects(self, other):
        o1 = self.orientation(other.a) 
        o2 = self.orientation(other.b) 
        o3 = other.orientation(self.a)
        o4 = other.orientation(self.b)
        if o1 != o2 and o3 != o4:
            return True
        if o1 == 0 and self.contains(other.a):
            return True
        if o2 == 0 and self.contains(other.b):
            return True
        if o3 == 0 and other.contains(self.a):
            return True
        if o4 == 0 and other.contains(self.b): 
            return True
        return False

    def distance_to_segment(self, other):
        if self.intersects(other):
            return 0.0
        return sqrt(min(
            other.distance2_to_point(self.a),
            other.distance2_to_point(self.b),
            self.distance2_to_point(other.a),
            self.distance2_to_point(other.b)
        ))

    def distance2_to_point(self, point):
        seg_len2 = self.length_squared()
        if seg_len2 == 0:
            return point.dist_squared(self.a)
        dot = (point.x - self.a.x) * (self.b.x - self.a.x) + (point.y - self.a.y) * (self.b.y - self.a.y)
        scale = max(0, min(1, dot / seg_len2))
        projection = Point(
            self.a.x + scale * (self.b.x - self.a.x), 
            self.a.y + scale * (self.b.y - self.a.y)
        )
        return point.dist_squared(projection)

def main():
    for _ in range(int(input())):
        a,b,c,d,e,f,g,h = map(int,input().split())
        l1 = LineSegment(a,b,c,d)
        l2 = LineSegment(e,f,g,h)
        dist = l1.distance_to_segment(l2)
        print('%.2f' % dist)

if __name__ == "__main__":
    main()