from collections import deque

class Graph:
    def __init__(self, v, edges):
        self.v = v
        self.edges = {_v: set() for _v in range(v)}
        self.init = [0]*v
        for a,b in edges:
            self.edges[a].add(b)
            self.edges[b].add(a)
            self.init[a] += 1
            self.init[b] += 1
        for i in range(v):
            self.init[i] //= 2

    def remove(self, u):
        queue = deque([u])
        visited = [False]*self.v
        visited[u] = True
        while queue:
            curr = queue.popleft()
            for neighbor in self.edges[curr]:
                self.edges[neighbor].remove(curr)
                if not visited[neighbor] and len(self.edges[neighbor]) <= self.init[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
            del self.edges[curr]

    def contains(self, u):
        return u in self.edges

def get_input():
    v,e,h,l = map(int,input().split())
    edges = ((lambda i: (int(i[0])-1, int(i[1])-1))(input().split()) for _ in range(e))
    return v,edges,h-1,l-1,

def main():
    v,edges,home,leaver = get_input()
    g = Graph(v,edges)
    g.remove(leaver)
    print('stay' if g.contains(home) else 'leave')

if __name__ == "__main__":
    main()
