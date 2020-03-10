from math import pi

class PolarSystem:
    def __init__(self, ts, rs, r):
        self.ts = ts
        self.rs = rs
        self.r = r
        self.rad_unit = 1/self.rs * self.r

    def find_shortest_path(self,t1,r1,t2,r2):
        if r1 == 0:
            return r2
        if r2 == 0:
            return r1
        if t1 == t2:
            return abs(r1-r2) * self.rad_unit
        return min(abs(t1-t2)*(r/self.rs)*self.r/self.ts * pi + (abs(r-r1) + abs(r-r2)) * self.rad_unit for r in range(0,self.rs+1))

def main():
    print(PolarSystem(*(lambda a,b,c: (int(a),int(b),float(c)))(*input().split())).find_shortest_path(*map(int,input().split())))

if __name__ == "__main__":
    main()