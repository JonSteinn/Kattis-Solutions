class UnionFind:
    def __init__(self, n):
        self.parent = [-1]*n
    
    def __find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.__find(self.parent[x])
        return self.parent[x]

    def connect(self, a, b):
        ra = self.__find(a)
        rb = self.__find(b)
        if ra == rb:
            return False
        if self.parent[ra] > self.parent[rb]:
            self.parent[rb] += self.parent[ra]
            self.parent[ra] = rb
        else:
            self.parent[ra] += self.parent[rb]
            self.parent[rb] = ra
        return True

def no_sort_kruskal(vertices, edges):
    uf = UnionFind(vertices)
    span_tree = []
    while edges and len(span_tree) < vertices-1:
        v,u,w = edges.pop()
        if not uf.connect(v,u):
            continue
        span_tree.append((v+1,u+1,w))
    if len(span_tree) != vertices-1:
        print('Impossible')
    else:
        for edge in span_tree:
            print(*edge)

def construct_edges(vertices):
    edges = []
    number_to_vertex = {}
    for v in range(vertices):
        _, *numbers = map(int,input().split())
        for w in numbers:
            if w not in number_to_vertex:
                number_to_vertex[w] = v
            else:
                edges.append((number_to_vertex[w],v,w))
    return edges

def main():
    vertices = int(input())
    edges = construct_edges(vertices)
    no_sort_kruskal(vertices,edges)

if __name__ == "__main__":
    main()