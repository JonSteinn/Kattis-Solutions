class Graph:
    @staticmethod
    def create_graph():
        c,r = map(int,input().split())
        mat = [list(map(int,input().split())) for _ in range(r)]
        return Graph(r,c,mat)

    def __init__(self, r, c, mat):
        self.r = r
        self.c = c
        self.mat = mat
        self.visited = [[False]*c for _ in range(r)]
        self.sinks = 0
        self._find_sinks()

    def _find_sinks(self):
        for _r in range(self.r):
            for _c in range(self.c):
                if not self.visited[_r][_c]:
                    self._expand([(_r,_c)])

    def _expand(self,stack):
        can_reach_less = False
        larger_stack = []
        cc_size = 0
        while stack:
            r,c = stack.pop()
            if self.visited[r][c]:
                continue
            self.visited[r][c] = True
            cc_size += 1

            if r > 0:
                if self.mat[r-1][c] == self.mat[r][c]:
                    stack.append((r-1,c))
                elif self.mat[r-1][c] < self.mat[r][c]:
                    can_reach_less = True
                else:
                    larger_stack.append((r-1,c))
            
            if r < self.r - 1:
                if self.mat[r+1][c] == self.mat[r][c]:
                    stack.append((r+1,c))
                elif self.mat[r+1][c] < self.mat[r][c]:
                    can_reach_less = True
                else:
                    larger_stack.append((r+1,c))

            if c > 0:
                if self.mat[r][c-1] == self.mat[r][c]:
                    stack.append((r,c-1))
                elif self.mat[r][c-1] < self.mat[r][c]:
                    can_reach_less = True
                else:
                    larger_stack.append((r,c-1))

            if c < self.c - 1:
                if self.mat[r][c+1] == self.mat[r][c]:
                    stack.append((r,c+1))
                elif self.mat[r][c+1] < self.mat[r][c]:
                    can_reach_less = True
                else:
                    larger_stack.append((r,c+1))

        if not can_reach_less:
            self.sinks += cc_size

        self._expand_larger(larger_stack)

    def _expand_larger(self,stack):
        while stack:
            r,c = stack.pop()
            if self.visited[r][c]:
                continue
            self.visited[r][c] = True
            if r > 0 and self.mat[r-1][c] == self.mat[r][c]:
                stack.append((r-1,c))
            if r < self.r - 1 and  self.mat[r+1][c] >= self.mat[r][c]:
                stack.append((r+1,c))
            if c > 0 and self.mat[r][c-1] >= self.mat[r][c]:
                stack.append((r,c-1))
            if c < self.c - 1 and self.mat[r][c+1] >= self.mat[r][c]:
                stack.append((r,c+1))

def main():
    print(Graph.create_graph().sinks)

if __name__ == "__main__":
    main()