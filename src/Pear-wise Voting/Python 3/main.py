class Graph:
    INF = 50

    def __init__(self, v):
        self.v = v
        self.mat = [[Graph.INF]*v for _ in range(v)]
        for i in range(v):
            self.mat[i][i] = 0

    def add_edge(self, v, u):
        self.mat[ord(v)-65][ord(u)-65] = 1

    def find_all_paths(self):
        # Floyd-Warshall
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    self.mat[i][j] = min(self.mat[i][j], self.mat[i][k]+self.mat[k][j])

    def contestent_status(self):
        for i in range(self.v):
            if Graph.INF in self.mat[i]:
                print(f'{chr(65+i)}: can\'t win')
            else:
                print(f'{chr(65+i)}: can win')

def vs_battle(ballots, c1, c2):
    w1,w2 = 0,0
    for ballot, count in ballots:
        if ballot[c1] < ballot[c2]:
            w1 += count
        else:
            w2 += count
    if w1 > w2:
        return c1,c2
    else:
        return c2,c1

def construct_graph(n,m):
    # list of tuples (dict, voters)
    # where dict maps candidate to position in ballot
    # Having lower position than other is a win for the ballot
    ballots = [({c: i for i,c in enumerate(b)},int(a)) for a,b in (input().split() for _ in range(m))]
    
    g = Graph(n)
    for i in range(1,n):
        for j in range(i):
            winner, looser = vs_battle(ballots, chr(65+i), chr(65+j))
            g.add_edge(winner, looser)
    
    g.find_all_paths()

    return g

def main():
    n,m = map(int,input().split())
    g = construct_graph(n,m)
    g.contestent_status()

if __name__ == "__main__":
    main()