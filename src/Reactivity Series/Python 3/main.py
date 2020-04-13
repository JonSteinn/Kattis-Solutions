from collections import deque

class Graph:
    def __init__(self,v,adj):
        self.vertices = v
        self.adj = adj

    def __recursive_helper(self,vertex,stack,visited):
        visited[vertex] = True
        for u in self.adj[vertex]:
            if not visited[u]:
                self.__recursive_helper(u,stack,visited)
        stack.appendleft(vertex)

    def topsort(self,src):
        visited = [False]*self.vertices
        stack = deque()
        self.__recursive_helper(src, stack, visited)
        if len(stack) != self.vertices:
            return ('back to the lab',)
        for i in range(self.vertices-1):
            if stack[i+1] not in self.adj[stack[i]]:
                return ('back to the lab',)
        return stack
            
def main():
    n,k = map(int,input().split())
    edges = [set() for _ in range(n)]
    in_order_zero = set(range(n))
    for _ in range(k):
        a,b = map(int,input().split())
        edges[a].add(b)
        in_order_zero.discard(b)

    g = Graph(n,edges)
    if len(in_order_zero) != 1:
        print('back to the lab')
    else:
        print(*g.topsort(in_order_zero.pop()))

if __name__ == "__main__":
    main()