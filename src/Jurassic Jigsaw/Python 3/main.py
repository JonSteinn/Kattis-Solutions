from heapq import heappop, heappush

class Graph:
    def __init__(self, n, adj):
        self.n = n
        self.adj = adj

    def mst(self):
        return self._prims()

    def _prims(self):
        # Init
        best = [0] * self.n
        remaining = set(range(1,self.n))
        visited = [True] + [False] * (self.n-1)
        heap = []
        edges = []
        dist = 0
        for i in range(1,self.n):
            heappush(heap, (self.adj[0][i], 0, i))
            best[i] = self.adj[0][i]

        # Search
        while len(edges) < self.n-1:
            while True:
                w, u, v = heappop(heap)
                if visited[v]: 
                    continue
                break
            edges.append((u,v))
            dist += w
            visited[v] = True
            remaining.remove(v)
            for x in remaining:
                if self.adj[v][x] < best[x]:
                    best[x] = self.adj[v][x]
                    heappush(heap, (self.adj[v][x], v, x))
        return dist, edges

def diff(str1,str2):
    return sum(a != b for a,b in zip(str1,str2))

def construct_adj(n):
    words = [None]*n
    adj = [[0]*n for _ in range(n)]
    for i in range(n):
        words[i] = input()
        for j in range(i):
            adj[j][i] = diff(words[j], words[i])
            adj[i][j] = adj[j][i]
    return adj

def main():
    n,_ = map(int,input().split())
    adj = construct_adj(n)
    g = Graph(n,adj)
    mst_len, mst = g.mst()
    print(mst_len)
    for edge in mst:
        print(*edge)

if __name__ == "__main__":
    main()