from math import atan2, asin, pi, sqrt
import bisect

# To handle float equality
EPSILON = 10**-6

class Subway:
    def __init__(self, n, d, points):
        self.n = n
        self.d = d
        self.points = points
        self.point_grps = []

    def minimal_covering_split(self):
        self.__split_into_possible_sub_regions()
        return sum(self.__mvc_subgroup(grp) for grp in self.point_grps)

    def __split_into_possible_sub_regions(self):
        """Since the points are sorted with respect to their angle, 
        we can group those together that are possibly using the same
        railway and solve for each sub problem. If two points have 
        an angle alpha between them and their max angle distance to
        a line is beta, then these can only possibly (but not necessarily)
        share a railroad if alpha is less than beta. Since we are on
        a circular field, we must also check if any in the first and
        last group are close enough.
        """
        lo,hi,l = (0,1,len(self.points))
        while hi < l:
            if self.points[hi-1].angle_diff(self.points[hi]) - EPSILON < \
                self.points[hi-1].max_angle_dist_to_line + self.points[hi].max_angle_dist_to_line:
                    hi += 1
            else:
                self.point_grps.append(self.points[lo:hi])
                lo,hi = (hi, hi + 1)
        self.point_grps.append(self.points[lo:hi])
        if len(self.point_grps) > 1:
            self.__join_first_and_last_if_close()
    
    def __join_first_and_last_if_close(self):
        """If any point in first group is within 'possible' distance of
        any point in the last group, we merge them, convert the angles of
        the last group into negative ones and re-sort the group.
        """
        for p1 in self.point_grps[0]:
            for p2 in self.point_grps[-1]:
                if p1.angle_diff(p2) - EPSILON < p1.max_angle_dist_to_line + p2.max_angle_dist_to_line:
                    l = len(self.point_grps[0])
                    self.point_grps[0].extend(self.point_grps.pop())
                    for new_p in self.point_grps[0][l:]:
                        new_p.angle -= 2*pi
                    self.point_grps[0].sort()
                    return

    def __mvc_subgroup(self, grp):
        """If there is no element in grp, then 0 railways are needed and if one, then one.
        Otherwise we start from one end (with respect to angles) and consume as many other
        points as we can and once we are outside the distance limit we use one railway for
        those close enough, and call the method recursively for the remaining ones. If the
        first and last element are close enough to share a railway, then there is only one
        needed to connect them all.
        """
        if len(grp) < 2:
            return len(grp)
        for i in range(1,len(grp)):
            if grp[0].angle_diff(grp[i]) - EPSILON > grp[0].max_angle_dist_to_line + grp[i].max_angle_dist_to_line:
                return 1 + self.__mvc_subgroup(grp[i:])
        return 1

class Point:
    """Everything here is self explanatory.
    """
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.angle = atan2(y,x)
        self.length = sqrt(x**2+y**2)
        if self.angle < 0:
            self.angle += 2*pi
        self.max_angle_dist_to_line = asin(d/self.length)
        if self.max_angle_dist_to_line < 0:
            self.max_angle_dist_to_line += 2*pi

    def angle_diff(self, larger):
        a_sum = larger.angle - self.angle
        if a_sum > pi:
            a_sum = 2*pi - a_sum
        return a_sum
        
    def __lt__(self, other):
        return self.angle < other.angle

def test_case(n,d):
    """Handle reading the points, filtering not needed and sorting the rest.
    """
    if n == 1:
        input() # Dump
        return '1'
    d_sq, points = (d**2, [])
    for _ in range(n):
        x,y = map(int, input().split())
        # Filter those that are close enough to the central station
        if x**2 + y**2 > d_sq:
            bisect.insort(points, Point(x,y,d))
    return Subway(n,d,points).minimal_covering_split()

def main():
    """Handles IO
    """
    for _ in range(int(input())):
        n,d = map(int, input().split())
        print(test_case(n,d))

if __name__ == "__main__":
    main()
