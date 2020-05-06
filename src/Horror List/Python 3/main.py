from collections import deque

class Graph:
    @staticmethod
    def construct_from_input():
        v,_,e = map(int,input().split())
        g = Graph(v)
        for s in map(int,input().split()):
            g.add_src(s)
        for _ in range(e):
            g.add_edge(*map(int,input().split()))
        return g            

    def __init__(self, vertices):
        self.adj = [[] for _ in range(vertices)]
        self.not_visited = set(range(vertices))
        self.queue = deque()

    def add_edge(self, v, u):
        self.adj[v].append(u)
        self.adj[u].append(v)

    def add_src(self, v):
        self.not_visited.remove(v)
        self.queue.append((0,v))

    def bfs(self):
        c,i = -1,-1
        while self.queue:
            cost, v = self.queue.popleft()
            if cost > c or (cost == c and v < i):
                c,i = cost, v
            for u in self.adj[v]:
                if u in self.not_visited:
                    self.not_visited.remove(u)
                    self.queue.append((cost+1,u))
        if not self.not_visited:
            return i
        else:
            return min(self.not_visited)

def main():
    print(Graph.construct_from_input().bfs())

if __name__ == "__main__":
    main()
