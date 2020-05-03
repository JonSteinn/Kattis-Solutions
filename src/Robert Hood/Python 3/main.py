from math import sqrt
from functools import cmp_to_key

class Point2d(tuple):
    def __new__(cls, x, y):
        return tuple.__new__(cls, (y, x))

    def __init__(self, y, x):
        pass

    def dist_sq(self, other):
        return (self[0]-other[0])**2 + (self[1]-other[1])**2

    def __str__(self):
        return str(tuple(reversed(self)))

    def orientation(self, p1, p2):
        t = (p1[0] - self[0]) * (p2[1] - p1[1]) - (p1[1] - self[1])*(p2[0]-p1[0])
        if t == 0:
            return 0 # colinear 
        if t > 0:
            return 1 # clockwise
        return 2 # counterclockwise 

    def angle_comparator(self, p1, p2):
        o = self.orientation(p1,p2)
        if o == 0:
            return -1 if self.dist_sq(p2) >= self.dist_sq(p1) else 1
        return -1 if o == 2 else 1
        
class ConvexHull:
    def __init__(self, n, pnts):
        self.convex_pnts = self._find_convex_hull(n, pnts)

    def _find_convex_hull(self, n, pnts):
        sw, all_pnts = self._construct_list_and_find_sw(pnts)
        all_pnts.sort(key=cmp_to_key(lambda p1, p2: sw.angle_comparator(p1,p2)), reverse=True)
        
        hull = [sw, all_pnts.pop()]
        while all_pnts:
            if sw.orientation(hull[-1], all_pnts[-1]) == 0:
                hull[-1] = all_pnts.pop()
                continue
            if len(hull) == 3:
                break
            hull.append(all_pnts.pop())

        # if len(hull) = 2, then not a ch but still works in this setup
        if not all_pnts:
            return hull

        while all_pnts:
            pnt = all_pnts.pop()
            while all_pnts and sw.orientation(pnt, all_pnts[-1]) == 0:
                pnt = all_pnts.pop()
            
            while hull[-2].orientation(hull[-1], pnt) != 2:
                hull.pop()
            hull.append(pnt)

        return hull

    def _construct_list_and_find_sw(self, pnts):
        j,sw = -1, Point2d(1001,1001)
        all_pnts = []
        for i,pnt in enumerate(pnts):
            if pnt < sw:
                sw = pnt
                j = i
            all_pnts.append(pnt)
        all_pnts[j] = all_pnts[-1]
        all_pnts.pop()
        return sw, all_pnts

    def longest_pair_path(self):
        longest = -1
        for i, p in enumerate(self.convex_pnts):
            for q in self.convex_pnts[i+1:]:
                longest = max(longest, p.dist_sq(q))
        return sqrt(longest)

def main():
    n = int(input())
    if n == 2:
        print('%.6f' % sqrt(Point2d(*map(int,input().split())).dist_sq(Point2d(*map(int,input().split())))))
    else:
        ch = ConvexHull(n, (Point2d(*map(int,input().split())) for _ in range(n)))
        print(ch.longest_pair_path())

if __name__ == "__main__":
    main()