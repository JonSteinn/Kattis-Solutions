from heapq import heappop, heappush

class Graph:
    class Edge:
        def __init__(self, to, t0, p, w):
            self.to = to
            self.t0 = t0
            self.p = p
            self.w = w

    def __init__(self, v, edges):
        self.v = v
        self.adj = [[] for _ in range(v)]
        for v,u,t0,p,w in edges:
            self.adj[v].append(Graph.Edge(u,t0,p,w))

    def neighbors_of_v_at_time_t(self, v, t):
        for edge in self.adj[v]:
            if t <= edge.t0:
                yield (edge.w + edge.t0-t, edge.to)
            elif edge.p:
                yield (edge.w + (edge.p - (t-edge.t0) % edge.p) % edge.p, edge.to)

class Djikstra:
    INF = 2147483647
    FAIL = 'Impossible'

    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.heap = [(0,s)]
        self.visited = [False] * g.v
        self.dist = [Djikstra.INF] * g.v
        self.dist[s] = 0
        self.visited[s] = True

    def shortest_path_to(self, v):
        if self.visited[v]:
            return str(self.dist[v])
        while self.heap:
            cc,cv = heappop(self.heap)
            self.visited[cv] = True
            for nc, nv in self.g.neighbors_of_v_at_time_t(cv,cc):
                d = cc + nc
                if d < self.dist[nv]:
                    self.dist[nv] = d
                    heappush(self.heap, (d, nv)) 
            if cv == v:
                return str(self.dist[v])
        return Djikstra.FAIL

def test_case(n,s,edges,queries):
    d = Djikstra(Graph(n,edges),s)
    print('\n'.join(d.shortest_path_to(vertex) for vertex in queries))

def get_test_cases():
    while True:
        n,m,q,s = map(int,input().split())
        if not n:
            break
        edges = (map(int,input().split()) for _ in range(m))
        queries = (int(input()) for _ in range(q))
        yield n, s, edges, queries

def main():
    first = True
    for test_case_data in get_test_cases():
        if first:
            first = False
        else:
            print()
        test_case(*test_case_data)

if __name__ == "__main__":
    main()