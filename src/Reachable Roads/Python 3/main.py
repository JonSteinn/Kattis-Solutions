class UnionFind:
    def __init__(self, n):
        self.components = n
        self.size = [1]*n
        self.parent = list(range(n))

    def __root(self,x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def connect(self,a,b):
        rA = self.__root(a)
        rB = self.__root(b)
        if rA == rB:
            return
        self.components -= 1
        if self.size[rA] < self.size[rB]:
            self.parent[rA] = rB
            self.size[rB] += self.size[rA]
        else:
            self.parent[rB] = rA
            self.size[rA] += self.size[rB]

    def number_of_components(self):
        return self.components

def city(e,r):
    uf = UnionFind(e)
    for _ in range(r):
        uf.connect(*map(int,input().split()))
    print(uf.number_of_components() - 1)

def main():
    for _ in range(int(input())):
        endpoints, roads = (int(input()), int(input()))
        city(endpoints, roads)

if __name__ == "__main__":
    main()