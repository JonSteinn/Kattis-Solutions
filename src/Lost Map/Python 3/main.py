from heapq import heappop, heappush, heapify

class Graph:
    def __init__(self, n, adj):
        self.n = n
        self.adj = adj

    def mst(self):
        self._prims()

    def _prims(self):
        best = [0] * self.n
        remaining = set(range(1,self.n))
        visited = [True] + [False] * (self.n-1)
        heap = []
        for i in range(1,self.n):
            heappush(heap, (self.adj[0][i], 0, i))
            best[i] = self.adj[0][i]
        edges = 0
        while edges < self.n-1:
            while True:
                _, u, v = heappop(heap)
                if visited[v]: 
                    continue
                break
            print(u+1,v+1)
            edges += 1
            visited[v] = True
            remaining.remove(v)
            for w in remaining:
                if self.adj[v][w] < best[w]:
                    best[w] = self.adj[v][w]
                    heappush(heap, (self.adj[v][w], v, w))

def main():
    n = int(input())
    adj = [list(map(int,input().split())) for _ in range(n)]
    g = Graph(n, adj)
    g.mst()

if __name__ == "__main__":
    main()