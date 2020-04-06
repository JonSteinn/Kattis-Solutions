from collections import deque

class Maze:
    class Node:
        UP    = 0
        RIGHT = 1
        DOWN  = 2
        LEFT  = 3

        def __init__(self,r,c,o):
            self.r = r
            self.c = c
            self.o = o

        def get_coords(self):
            return (self.r,self.c)

    def __init__(self, cells, h, w):
        self.cells = cells
        self.h = h
        self.w = w
        self.start = None
        self.end = None
        self.no_solution = False
        self.unreachable_cells = False
        self.multiple_paths = False
        self.__validate()

    def __validate(self):
        self.__find_exits()
        self.__dfs()

    def __find_exits(self):
        for check in (self.__check_up, self.__check_down, self.__check_left, self.__check_right):
            check()
            if self.start is not None and self.end is not None:
                break
        #assert(self.start is not None)
        #assert(self.end is not None)

    def __check_up(self):
        for c,x in enumerate(self.cells[0]):
            if not int(x,base=16) & 0b1000:
                if self.start is None:
                    self.start = (0,c,Maze.Node.DOWN)
                else:
                    self.end = (0,c)
                    return

    def __check_down(self):
        for c,x in enumerate(self.cells[-1]):
            if not int(x,base=16) & 0b0010:
                if self.start is None:
                    self.start = (self.h-1,c,Maze.Node.UP)
                else:
                    self.end = (self.h-1,c)
                    return

    def __check_left(self):
        for i in range(self.h):
            if not int(self.cells[i][0],base=16) & 0b0001:
                if self.start is None:
                    self.start = (i,0,Maze.Node.RIGHT)
                else:
                    self.end = (i,0)
                    return

    def __check_right(self):
        for i in range(self.h):
            if not int(self.cells[i][self.w-1],base=16) & 0b0100:
                if self.start is None:
                    self.start = (i,self.w-1,Maze.Node.LEFT)
                else:
                    self.end = (i,self.w-1)
                    return

    def __dfs(self):
        visited = set()
        stack = deque()
        stack.append(Maze.Node(*self.start))
        while stack:
            curr = stack.pop()
            curr_pos = curr.get_coords()
            if curr_pos not in visited:
                visited.add(curr_pos)
                for neighbor in self.__get_neighbors(curr):
                    stack.append(neighbor)
            else:
                self.multiple_paths = True
        if self.end not in visited:
            self.no_solution = True
        if len(visited) != self.h * self.w:
            self.unreachable_cells = True

    def __get_neighbors(self, node):
        val = int(self.cells[node.r][node.c],base=16)
        if not val & 0b1000 and node.o != Maze.Node.DOWN and node.r > 0:
            yield Maze.Node(node.r-1,node.c,Maze.Node.UP)
        if not val & 0b0100 and node.o != Maze.Node.LEFT and node.c < self.w - 1:
            yield Maze.Node(node.r,node.c+1,Maze.Node.RIGHT)
        if not val & 0b0010 and node.o != Maze.Node.UP and node.r < self.h - 1:
            yield Maze.Node(node.r+1,node.c,Maze.Node.DOWN)
        if not val & 0b0001 and node.o != Maze.Node.RIGHT and node.c > 0:
            yield Maze.Node(node.r,node.c-1,Maze.Node.LEFT)

    def status(self):
        if self.no_solution:
            return 'NO SOLUTION'
        elif self.unreachable_cells:
            return 'UNREACHABLE CELL'
        elif self.multiple_paths:
            return 'MULTIPLE PATHS'
        else:
            return 'MAZE OK'

def main():
    while True:
        h,w = map(int,input().split())
        if h + w == 0:
            break
        print(Maze([input() for _ in range(h)],h,w).status())

if __name__ == "__main__":
    main()