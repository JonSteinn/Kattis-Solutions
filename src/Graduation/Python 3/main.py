class UnionFind:
    def __init__(self, size):
        self._parent = [-1] * size
        self._grps = size

    def find(self, idx):
        if self._parent[idx] < 0:
            return idx
        self._parent[idx] = self.find(self._parent[idx])
        return self._parent[idx]

    def size(self, idx):
        return -self._parent[self.find(idx)]

    def connect(self, idx1, idx2):
        idx1, idx2 = self.find(idx1), self.find(idx2)
        if idx1 == idx2:
            return False
        if self.size(idx1) > self.size(idx2):
            idx1, idx2 = idx2, idx1
        self._parent[idx2] += self._parent[idx1]
        self._parent[idx1] = idx2
        self._grps -= 1
        return True

    def groups(self):
        return self._grps

def main():
    n, _, k = map(int, input().split())
    uf = UnionFind(k)
    for col in zip(*(input() for _ in range(n))):
        for a, b in zip(col, col[1:]):
            uf.connect(ord(a)-65, ord(b)-65)
    print(uf.groups())

if __name__ == "__main__":
    main()
