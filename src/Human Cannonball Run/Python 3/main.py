from math import sqrt


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return sqrt((self.x - other.x)**2 + (self.y-other.y)**2)
    

class Graph:

    def __init__(self, n):
        self.n = n
        self.circles = []
        self.dist = [[0] * self.n for _ in range(self.n)]

    def add_node(self, circle):
        self.circles.append(circle)

    def calculate_edges(self):
        for i in range(1,self.n-1):
            # Pos to canons
            self.dist[0][i] = self.circles[0].distance_to(self.circles[i])
            self.dist[self.n-1][i] = self.circles[self.n-1].distance_to(self.circles[i])
            # Cannons to pos
            self.dist[i][0] = min(self.dist[0][i], 10 + abs(50 - self.dist[0][i]))
            self.dist[i][self.n-1] = min(self.dist[self.n-1][i], 10 + abs(50 - self.dist[self.n-1][i]))
        # Pos to pos
        self.dist[0][self.n-1] = self.circles[0].distance_to(self.circles[self.n-1])
        self.dist[self.n-1][0] = self.dist[0][self.n-1]

        # Canons to canons
        for i in range(1,self.n-1):
            for j in range(i+1,self.n-1):
                if i != j:
                    d = self.circles[i].distance_to(self.circles[j])
                    d = min(d, 10 + abs(50 - d))
                    self.dist[i][j] = d
                    self.dist[j][i] = d

    def floyd_warshall(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][k]+self.dist[k][j])

    def shortest_path_time(self):
        return self.dist[0][self.n-1] / 5

def construct_graph_from_input():
    s_x,s_y = map(float,input().split())
    e_x,e_y = map(float,input().split())
    n = int(input())
    g = Graph(n+2)
    g.add_node(Position(s_x,s_y))
    for _ in range(n):
        g.add_node(Position(*map(float,input().split())))
    g.add_node(Position(e_x,e_y))
    return g

def main():
    g = construct_graph_from_input()
    g.calculate_edges()
    g.floyd_warshall()
    print('%.4f' % g.shortest_path_time())

if __name__ == "__main__":
    main()