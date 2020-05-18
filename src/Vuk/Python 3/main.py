from collections import deque
from heapq import heappop, heappush

class Graph:
    # One will suffice as all weights will be stored as negatives in heap
    INF = 1

    @staticmethod
    def create_from_input():
        r,c = map(int,input().split())
        mat = [input() for _ in range(r)]
        return Graph(r,c,mat)

    def __init__(self,r,c,mat):
        self.r = r
        self.c = c
        self.mat = mat
        self.wolf, self.cottage, trees = self._find_objects()
        self.dist = self._create_distance_mat(trees)

    def _find_objects(self):
        queue = deque()
        for r, row in enumerate(self.mat):
            for c, x in enumerate(row):
                if x == '+':
                    queue.append((r,c,0))
                elif x == 'V':
                    wolf = (r,c)
                elif x == 'J':
                    cottage = (r,c)
        return wolf, cottage, queue

    def _create_init_dist_mat(self,queue):
        mat = [[-1] * self.c for _ in range(self.r)]
        for r,c,_ in queue:
            mat[r][c] = 0
        return mat

    def _create_distance_mat(self,queue):
        mat = self._create_init_dist_mat(queue)
        while queue:
            r,c,dist = queue.popleft()
            for n_r,n_c in self._get_neighbors(r,c):
                if mat[n_r][n_c] == -1:
                    mat[n_r][n_c] = dist+1
                    queue.append((n_r,n_c,dist+1))
        return mat

    def _get_neighbors(self,r,c):
        if r > 0:
            yield (r-1,c)
        if r < self.r-1:
            yield (r+1,c)
        if c > 0:
            yield (r,c-1)
        if c < self.c-1:
            yield (r,c+1)

    def _djikstra_init(self):
        best = [[Graph.INF]*self.c for _ in range(self.r)]
        w_r,w_c = self.wolf
        best[w_r][w_c] = -self.dist[w_r][w_c]
        p_queue = [(-self.dist[w_r][w_c],w_r,w_c)]
        return best, p_queue

    def min_dist_to_trees(self):
        best, queue = self._djikstra_init()

        while queue:
            dist, r, c = heappop(queue)
            
            if (r,c) == self.cottage:
                return -dist

            for n_r,n_c in self._get_neighbors(r,c):
                # Lets just ignore those let an empty queue correspond to
                # having to travel through one of these. Anything to reduce
                # the queue size ultimately helps...
                if self.mat[n_r][n_c] == '+':
                    continue

                n_d = max(dist, -self.dist[n_r][n_c])

                if n_d < best[n_r][n_c]:
                    heappush(queue, (n_d,n_r,n_c))
                    best[n_r][n_c] = n_d

        return 0

def main():
    g = Graph.create_from_input()
    print(g.min_dist_to_trees())

if __name__ == "__main__":
    main()