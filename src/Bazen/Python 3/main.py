class Triangle:
    AREA = 31250
    
    CORNERS = {
        (0,0): (125,125),
        (250,0): (0,125),
        (0,250): (125,0),
        (125,125): (0,0),
        (0,125): (250,0),
        (125,0): (0,250)
    }

    @staticmethod
    def h_to_d(x):
        # looking for a point (z,250-z) such that him and (x,0) & 
        # (250,0) for a trianle with half the area of the original
        # 
        # abs(x*(z-250)+250*(250-z))/2 = half_area
        # abs(x*(z-250)+250*(250-z)) = area
        # x*(z-250)+250*(250-z) = pm area
        # z = ((pm area) + 250*x-250**2)/(x-250)
        #
        # Since x is in [1,124] here, we can also narrow it 
        # down to a single solution of positive area.
        #
        # Similar logic done for rest...
        return (lambda z: (z, 250-z))((Triangle.AREA + 250*x-250**2)/(x-250))

    @staticmethod
    def h_to_v(x):
        return 0, Triangle.AREA / x

    @staticmethod
    def v_to_d(y):
        return (lambda z: (z, 250-z))(Triangle.AREA / (250-y))

    @staticmethod
    def v_to_h(y):
        return Triangle.AREA/y, 0

    @staticmethod
    def d_to_v(x,y):
        return 0, 250 - Triangle.AREA/x

    @staticmethod
    def d_to_h(x,y):
        return (250*y - Triangle.AREA)/y, 0
    
    @staticmethod
    def find_other(x,y):
        if (x,y) in Triangle.CORNERS:
            return Triangle.CORNERS[(x,y)]
        elif x == 0:
            return Triangle.v_to_d(y) if y < 125 else Triangle.v_to_h(y)
        elif y == 0:
            return Triangle.h_to_d(x) if x < 125 else Triangle.h_to_v(x)
        else:
            return Triangle.d_to_h(x,y) if x < 125 else Triangle.d_to_v(x,y)
            
def main():
    print('%.2f %.2f' % Triangle.find_other(*map(int,input().split())))

if __name__ == "__main__":
    main()