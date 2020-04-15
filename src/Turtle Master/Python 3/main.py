from collections import deque

class Orientation:
    RIGHT,DOWN,LEFT,UP = range(4)

    def __init__(self):
        self.o = Orientation.RIGHT

    def rotate_right(self):
        self.o = (self.o + 1) % 4

    def rotate_left(self):
        self.o = (self.o + 3) % 4

    def forward(self,x,y):
        if self.o == Orientation.RIGHT:
            return x+1,y
        if self.o == Orientation.LEFT:
            return x-1,y
        if self.o == Orientation.UP:
            return x,y+1
        return x,y-1

def out_of_bounds(x,y):
    return x < 0 or x > 7 or y < 0 or y > 7

def simulate(mat, seq):
    ERROR, SUCCESS = 'Bug!', 'Diamond!'
    o,x,y = Orientation(),0,0
    diamond = (-1,-1)
    for cmd in seq:
        if cmd == 'F':
            _x,_y = o.forward(x,y)
            if out_of_bounds(_x,_y):
                return ERROR
            if mat[_y][_x] == 'D':
                diamond = (_x,_y)
                mat[_y][_x] == 'T'
                x,y = _x,_y
                continue
            if mat[_y][_x] != '.':
                return ERROR
            else:
                mat[y][x] = '.'
                mat[_y][_x] = 'T'
                x,y = _x,_y
        elif cmd == 'R':
            o.rotate_right()
        elif cmd == 'L':
            o.rotate_left()
        else:
            _x,_y = o.forward(x,y)
            if out_of_bounds(_x,_y):
                return ERROR
            if mat[_y][_x] == 'I':
                mat[_y][_x] = '.'
            else:
                return ERROR
    return SUCCESS if (x,y) == diamond else ERROR

def main():
    mat = deque()
    for _ in range(8):
        mat.appendleft(list(input()))
    seq = input()
    print(simulate(mat,seq))

if __name__ == "__main__":
    main()