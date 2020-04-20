from math import sqrt
from heapq import heappop, heappush

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Graph:
    @staticmethod
    def construct_adj(points, n):
        adj = [[0.0]*n for _ in range(n)]
        for i,c1 in enumerate(points):
            for j,c2 in enumerate(points[i+1:]):
                dist = c1.distance_to(c2)
                adj[i][i+j+1] = dist
                adj[i+j+1][i] = dist
        return adj

    def __init__(self, n, points):
        self.n = n
        self.adj = Graph.construct_adj(points,n)

    def mst(self):
        return self._prims()

    def _prims(self):
        best = [0] * self.n
        remaining = set(range(1,self.n))
        visited = [True] + [False] * (self.n-1)
        heap = []
        for i in range(1,self.n):
            heappush(heap, (self.adj[0][i], i))
            best[i] = self.adj[0][i]
        edges, dist = 0, 0.0
        while edges < self.n - 1:
            while True:
                w, v = heappop(heap)
                if visited[v]: 
                    continue
                break
            dist += w
            visited[v] = True
            edges += 1
            remaining.remove(v)
            for w in remaining:
                if self.adj[v][w] < best[w]:
                    best[w] = self.adj[v][w]
                    heappush(heap, (self.adj[v][w], w))
        return dist

def test_case(n):
    points = [Point(*map(float,input().split())) for _ in range(n)]
    g = Graph(n, points)
    print('%.2f' % g.mst())

def main():
    for i in range(int(input())):
        if i:
            print()
        input()
        n = int(input())
        test_case(n)

if __name__ == "__main__":
    main()