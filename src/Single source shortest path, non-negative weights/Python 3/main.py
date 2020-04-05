from collections import defaultdict
from heapq import heappop, heappush

class Graph:
    INF = 2147483647

    def __init__(self, n, s):
        self.root = s
        self.distance = [Graph.INF]*n
        self.edges = defaultdict(dict)

    def add_edge(self, u, v, w):
        self.edges[u][v] = w

    def distance_to(self, v):
        if self.distance[v] == Graph.INF:
            return 'Impossible'
        else:
            return self.distance[v]

    def djikstra(self):
        queue = [(0,self.root)]
        self.distance[self.root] = 0
        while queue:
            cost,vertex = heappop(queue)
            for neighbor, weight in self.edges[vertex].items():
                if cost + weight < self.distance[neighbor]:
                    self.distance[neighbor] = cost + weight
                    heappush(queue, (cost + weight, neighbor))

def test_case(n,m,q,s):
    graph = Graph(n, s)
    for _ in range(m):
        graph.add_edge(*map(int,input().split()))
    graph.djikstra()
    for _ in range(q):
        print(graph.distance_to(int(input())))

def main():
    while True:
        n,m,q,s = map(int,input().split())
        if n == m == q == s == 0:
            break
        test_case(n,m,q,s)
        print()

if __name__ == "__main__":
    main()