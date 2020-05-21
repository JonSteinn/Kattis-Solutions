from math import sqrt, acos, pi, sin

def csc(x):
    return 1/sin(x)

# Using this as Vec2d too
class Point2d(tuple):
    def __new__(cls, x, y):
        return tuple.__new__(cls, (x,y))

    def dist_to(self, other):
        return sqrt(sum((a-b)**2 for a,b in zip(self,other)))

    def scale(self, c):
        return Point2d(self[0]*c, self[1]*c)

    def vector_to(self, other):
        return Point2d(other[0]-self[0], other[1]-self[1])

    def __add__(self, other):
        return Point2d(self[0]+other[0],self[1]+other[1])

class Triangle:
    DEG_120 = 2*pi/3
    DEG_60 = pi/3

    @staticmethod
    def create_from_input():
        return Triangle(
            Point2d(*map(int,input().split())),
            Point2d(*map(int,input().split())),
            Point2d(*map(int,input().split())),
        )

    def __init__(self, a, b, c):
        # vertices
        self.pa = a
        self.pb = b
        self.pc = c
        # sides
        self.a = b.dist_to(c)
        self.b = a.dist_to(c)
        self.c = a.dist_to(b)
        # angles
        self.A = acos((self.b**2+self.c**2-self.a**2)/(2*self.b*self.c))
        self.B = acos((self.a**2+self.c**2-self.b**2)/(2*self.a*self.c))
        self.C = acos((self.a**2+self.b**2-self.c**2)/(2*self.a*self.b))

    def fermat_point(self):
        if self.A >= Triangle.DEG_120:
            return self.pa
        if self.B >= Triangle.DEG_120:
            return self.pb
        if self.C >= Triangle.DEG_120:
            return self.pc

        x = csc(self.A + Triangle.DEG_60)
        y = csc(self.B + Triangle.DEG_60)
        z = csc(self.C + Triangle.DEG_60)

        v_ca = self.pc.vector_to(self.pa)
        v_cb = self.pc.vector_to(self.pb)

        d = self.a * x + self.b * y + self.c * z

        return v_ca.scale(self.a * x / d) + v_cb.scale(self.b * y / d) + self.pc

def main():
    print(*Triangle.create_from_input().fermat_point())

if __name__ == "__main__":
    main()