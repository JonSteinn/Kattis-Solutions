class Point(tuple):
    def __new__(cls, x, y):
        return tuple.__new__(cls, (x,y))

    def distance_square_to(self, other):
        return sum((a-b)**2 for a,b in zip(self, other))

class Circle:
    def __init__(self, x, y, r):
        self.c = Point(x,y)
        self.r = r
        self.rsq = r*r

    def contains(self, pnt):
        return self.c.distance_square_to(pnt) <= self.rsq

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.x2 = x+w
        self.y1 = y
        self.y2 = y+h

    def contains(self, pnt):
        return self.x1 <= pnt[0] <= self.x2 and self.y1 <= pnt[1] <= self.y2

class RoundedRectangle:
    def __init__(self, x, y, w, h, r):
        self.containing_rect = Rectangle(x,y,w,h)
        self.corner_rects = [
            Rectangle(x,y,r,r),         # NW
            Rectangle(x+w-r,y,r,r),     # NE
            Rectangle(x+w-r,y+h-r,r,r), # #SE
            Rectangle(x,y+h-r,r,r)      # SW
        ]
        self.corner_circles = [
            Circle(x+r,y+r,r),      # NW
            Circle(x+w-r,y+r,r),    # NE
            Circle(x+w-r,y+h-r,r),  # SE
            Circle(x+r,y+h-r,r)     # SW
        ]

    def contains(self, pnt):
        if not self.containing_rect.contains(pnt):
            return False
        for r,c in zip(self.corner_rects, self.corner_circles):
            if r.contains(pnt) and not c.contains(pnt):
                return False
        return True

def test_case(rrect,pnt_cnt,pnts):
    print('\n'.join(('inside' if rrect.contains(Point(next(pnts),next(pnts))) else 'outside' for _ in range(pnt_cnt))), end='\n\n')

def main():
    for _ in range(int(input())):
        x,y,w,h,r,pnt_cnt,*pnts = input().split()
        test_case(RoundedRectangle(float(x),float(y),float(w),float(h),float(r)),int(pnt_cnt), map(float, pnts))
        
if __name__ == "__main__":
    main()