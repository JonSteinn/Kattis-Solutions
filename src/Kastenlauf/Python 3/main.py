class Graph:
    def __init__(self):
        self.edges = {}

    def add_vertex(self, x,y):
        self.edges[(x,y)] = set()
        for a,b in self.edges.keys():
            if a == x and b == y:
                continue
            if abs(a-x) + abs(b-y) <= 1000:
                self.edges[(a,b)].add((x,y))
                self.edges[(x,y)].add((a,b))
        
    def has_path(self, from_x, from_y, to_x, to_y):
        visited = set()
        stack = [(from_x,from_y)]
        while stack:
            c_x,c_y = stack.pop()
            if c_x == to_x and c_y == to_y:
                return True
            if (c_x,c_y) in visited:
                continue
            visited.add((c_x,c_y))
            for x,y in self.edges[(c_x,c_y)]:
                if (x,y) not in visited:
                    stack.append((x,y))
        return False

def main():
    for _ in range(int(input())):
        graph = Graph()
        n = int(input())
        start_x,start_y = map(int,input().split())
        graph.add_vertex(start_x,start_y)
        for _ in range(n):
            x,y = map(int,input().split())
            graph.add_vertex(x,y)
        end_x,end_y = map(int,input().split())
        graph.add_vertex(end_x,end_y)
        if graph.has_path(start_x,start_y,end_x,end_y):
            print('happy')
        else:
            print('sad')

if __name__ == "__main__":
    main()