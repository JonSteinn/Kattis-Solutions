from heapq import heappop, heappush, heapify

class Graph:
    def __init__(self, n, adj):
        self.n = n
        self.adj = adj

    def mst(self,m):
        return 'yes' if self._prims(m) else 'no'

    def _prims(self,m):
        best = [0] * self.n
        remaining = set(range(1,self.n))
        visited = [True] + [False] * (self.n-1)
        heap = []
        edges, dist = 0,0
        for i in range(1,self.n):
            heappush(heap, (self.adj[0][i], i))
            best[i] = self.adj[0][i]
        while edges < self.n-1:
            while True:
                w, v = heappop(heap)
                if visited[v]: 
                    continue
                break
            edges += 1
            dist += w
            if dist + self.n > m:
                return False
            visited[v] = True
            remaining.remove(v)
            for w in remaining:
                if self.adj[v][w] < best[w]:
                    best[w] = self.adj[v][w]
                    heappush(heap, (self.adj[v][w], w))
        return self.n + dist <= m

def read_adj(c,adj):
    for _ in range((c*(c-1))//2):
        u,v,w = map(int,input().split())
        adj[u][v] = w
        adj[v][u] = w

def test_case(m,c):
    adj = [[0]*c for _ in range(c)]
    read_adj(c,adj)
    if m < c:
        print('no')
    else:
        g = Graph(c, adj)
        print(g.mst(m))

def main():
    for _ in range(int(input())):
        m,c = map(int,input().split())
        test_case(m,c)

if __name__ == "__main__":
    main()