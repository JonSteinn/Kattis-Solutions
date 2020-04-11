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

def kruskal(vertices, edges):
    uf = UnionFind(vertices)
    total_w = 0
    mst = []
    while edges and len(mst) < vertices-1:
        u,v,w = edges.pop()
        if not uf.connect(u,v):
            continue
        total_w += w
        mst.append((u,v) if u < v else (v,u))
    if len(mst) != vertices-1:
        print('Impossible')
    else:
        print(total_w)
        for edge in sorted(mst):
            print(*edge)

def main():
    while True:
        v, e = map(int,input().split())
        if v + e == 0:
            break
        edges = sorted(
            (tuple(map(int, input().split())) for _ in range(e)),
            key=lambda z: z[2],
            reverse=True
        )
        kruskal(v,edges)

if __name__ == "__main__":
    main()