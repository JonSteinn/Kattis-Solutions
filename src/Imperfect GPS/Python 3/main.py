from math import sqrt

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distance_to(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def __str__(self):
        return f'({self.x},{self.y})'

def find_len(positions, n):
    actual_len = 0.0
    last = -1
    for _ in range(n):
        x,y,_t = map(int,input().split())
        positions[_t] = Point(x,y)
        if last != -1:
            actual_len += positions[last].distance_to(positions[_t])
        last = _t
    return actual_len, last

# we know we won't find the element so always the next one...
def binary_search_least_not_smaller(sorted_times, _len, t):
    l,r = 0, _len-1
    while l <= r:
        m = l + (r-l)//2
        if sorted_times[m] < t:
            l = m+1
        else:
            r = m-1
    return l

def interpolate_point(sorted_times, positions, gps_time):
    index_above = binary_search_least_not_smaller(sorted_times, len(sorted_times), gps_time)
    right = sorted_times[index_above]
    left = sorted_times[index_above - 1]

    l_ratio = (right-gps_time)/(right-left)
    r_ratio = 1- l_ratio

    return Point(
        positions[left].x * l_ratio + positions[right].x * r_ratio,
        positions[left].y * l_ratio + positions[right].y * r_ratio
    )

def find_gps_len(positions,t,last):
    sorted_times = list(positions.keys()) # read inorder, and keys in >=3.6 maintain add order

    gps_len = 0.0
    gps_time = t
    stop_loop = False
    last_coord = positions[0] # always starts on 0
    while not stop_loop:
        if gps_time >= last:
            gps_time = last
            stop_loop = True
        
        if gps_time in positions:
            gps_len += last_coord.distance_to(positions[gps_time])
            last_coord = positions[gps_time]
        else:
            tmp = interpolate_point(sorted_times, positions, gps_time)
            gps_len += last_coord.distance_to(tmp)
            last_coord = tmp

        gps_time += t

    return gps_len

def main():
    n,t = map(int,input().split())
    positions = {}

    actual_len, last = find_len(positions,n)
    gps_len = find_gps_len(positions,t,last)

    print('%.5f' % (100-100*gps_len/actual_len))


if __name__ == "__main__":
    main()