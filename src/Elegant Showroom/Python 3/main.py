from heapq import heappop, heappush

class Graph:
    DOOR = 'D'
    WALL = '#'

    def _construct_exit_queue(self):
        q = []
        for _r in range(self.r):
            if self.mat[_r][0] == Graph.DOOR:
                q.append((0,_r,0))
            if self.mat[_r][self.c-1] == Graph.DOOR:
                q.append((0,_r,self.c-1))
        for _c in range(1,self.c-1):
            if self.mat[0][_c] == Graph.DOOR:
                q.append((0,0,_c))
            if self.mat[self.r-1][_c] == Graph.DOOR:
                q.append((0,self.r-1,_c))
        return q

    def __init__(self,r,c,mat):
        self.r = r
        self.c = c
        self.mat = mat
        self.queue = self._construct_exit_queue()

    def _neighbors(self,r,c):
        if r > 0 and self.mat[r-1][c] != Graph.WALL:
            yield (r-1,c)
        if r < self.r-1 and self.mat[r+1][c] != Graph.WALL:
            yield (r+1,c)
        if c > 0 and self.mat[r][c-1] != Graph.WALL:
            yield (r,c-1)
        if c < self.c-1 and self.mat[r][c+1] != Graph.WALL:
            yield (r,c+1)

    def _is_goal(self,r,c):
        return (r == 0 or r == self.r-1 or c == 0 or c == self.c-1) and self.mat[r][c] == Graph.DOOR

    def shortet_path(self,r,c):
        visited = [[False] * self.c for _ in range(self.r)]
        while self.queue:
            curr_cost, curr_r,curr_c = heappop(self.queue)
            if curr_r == r and curr_c == c:
                return curr_cost
            if visited[curr_r][curr_c]:
                continue
            visited[curr_r][curr_c] = True
            for n_r,n_c in self._neighbors(curr_r, curr_c):
                if not visited[n_r][n_c]:
                    heappush(self.queue, (curr_cost if self.mat[n_r][n_c] == Graph.DOOR else curr_cost + 1, n_r, n_c))
        return -1
        
def main():
    r,c = map(int,input().split())
    g = Graph(r,c, [input() for _ in range(r)])
    sr,sc = map(int,input().split())
    print(g.shortet_path(sr-1,sc-1))

if __name__ == "__main__":
    main()