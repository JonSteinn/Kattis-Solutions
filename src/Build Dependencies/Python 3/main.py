from collections import deque

class Graph:
    def __init__(self):
        self.next_index = 0
        self.names = []
        self.vertices = {}
        self.edges = {}
        self.rev_edges = {}
        self.vertices_used = set()
        self.changed = -1

    def add_dependencies(self, src, dsts):
        if src not in self.vertices:
            self.names.append(src)
            self.vertices[src] = self.next_index
            self.edges[self.next_index] = set()
            self.rev_edges[self.next_index] = set()
            self.next_index += 1
        j = self.vertices[src]
        for d in dsts:
            if d not in self.vertices:
                self.names.append(d)
                self.vertices[d] = self.next_index
                self.edges[self.next_index] = set()
                self.rev_edges[self.next_index] = set()
                self.next_index += 1
            k = self.vertices[d]
            self.edges[k].add(j)
            self.rev_edges[j].add(k)

    def change(self, src):
        self.changed = self.vertices[src]

    def init_dfs(self):
        stack = deque([self.changed])
        while stack:
            curr = stack.pop()
            if curr in self.vertices_used:
                continue
            self.vertices_used.add(curr)
            for v in self.edges[curr]:
                stack.append(v)

    def dependencies(self):
        stack = deque([(-1, self.changed)])
        while stack:
            parent,curr = stack.pop()
            if parent != -1:
                self.rev_edges[curr].remove(parent)
                if any(i in self.vertices_used for i in self.rev_edges[curr]):
                    continue
            print(self.names[curr])
            for v in self.edges[curr]:
                stack.append((curr,v))
        
def main():
    g = Graph()
    for _ in range(int(input())):
        dst,*src = input().split()
        g.add_dependencies(dst[:-1], src)
    g.change(input().rstrip())
    g.init_dfs()
    g.dependencies()
    
if __name__ == "__main__":
    main()