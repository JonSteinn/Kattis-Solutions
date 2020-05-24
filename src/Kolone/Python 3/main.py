class Ant(str):
    LEFT, RIGHT = range(2)

    @staticmethod
    def create_left_ant(string):
        return Ant(string,Ant.LEFT)

    @staticmethod
    def create_right_ant(string):
        return Ant(string,Ant.RIGHT)

    def __new__(cls, string, direction):
        return str.__new__(cls, string)
    
    def __init__(self, string, direction):
        self.dir = direction

    def is_left(self):
        return self.dir == Ant.LEFT
    
    def is_right(self):
        return self.dir == Ant.RIGHT
    
def read_and_proccess_input():
    l,r = map(int,input().split())
    lis = list(map(Ant.create_right_ant, input()[::-1]))
    lis.extend(list(map(Ant.create_left_ant, input())))
    t = int(input())
    r = set(range(l,l+r))
    l = set(range(l))
    return l,r,t,lis

def swap(lis, i, j):
    tmp = lis[i]
    lis[i] = lis[j]
    lis[j] = tmp

def simulate_round(l,r,lis):
    lcpy = l.copy()
    r_swap_this_round = set()
    no_swaps = True
    while lcpy:
        curr_l = lcpy.pop()
        if curr_l+1 in r and curr_l+1 not in r_swap_this_round:
            r.remove(curr_l+1)
            r.add(curr_l)
            l.remove(curr_l)
            l.add(curr_l+1)
            r_swap_this_round.add(curr_l)
            swap(lis, curr_l, curr_l+1)
            no_swaps = False
    return no_swaps

def main():
    l,r,t,lis = read_and_proccess_input()
    for _ in range(t):
        if simulate_round(l,r,lis):
            break
    print(''.join(lis))

if __name__ == "__main__":
    main()