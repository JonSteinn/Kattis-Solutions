class State(int):
    NONE = 0
    DOWN = 1
    RIGHT = 2

    @staticmethod
    def none():
        return State(State.NONE)

    @staticmethod
    def down():
        return State(State.DOWN)

    @staticmethod
    def right():
        return State(State.RIGHT)
    
    @staticmethod
    def down_and_right():
        return State(State.RIGHT | State.DOWN)

    def __new__(cls, x):
        return int.__new__(cls, x)

    def r(self):
        return self & State.RIGHT != 0

    def d(self):
        return self & State.DOWN != 0

def check_square(r, d, x):
    if x == 'A':
        if r or d:
            return False, State.none()
        else:
            return True, State.none()
    elif x == 'B':
        if r and not d:
            return True, State.right()
        elif d and not r:
            return True, State.down()
        else:
            return False, State.none()
    elif x == 'C':
        if r and d:
            return True, State.none()
        elif r:
            return True, State.down()
        elif d:
            return True, State.right()
        else:
            return True, State.down_and_right()
    else:
        if r and d:
            return True, State.down_and_right()
        else:
            return False, State.none()

def pipe_check_row(row,states):
    for c,x in enumerate(row):
        r, d = c != 0 and states[c-1].r(), states[c].d()
        valid, state = check_square(r,d,x)
        if not valid:
            return False
        states[c] = state
    return not states[-1].r() 

def pipe_check(c,mat):
    states = [State.none() for _ in range(c)]
    for row in mat:
        if not pipe_check_row(row,states):
            return False
    return all(not s.d() for s in states)
    
def main():
    r,c = map(int,input().split())
    mat = [input() for _ in range(r)]
    print('Possible' if pipe_check(c,mat) else 'Impossible')

if __name__ == "__main__":
    main()