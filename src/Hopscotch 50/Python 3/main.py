from heapq import heappop, heappush

class Graph:
    INF = 2147483647

    @staticmethod
    def create_from_input():
        n,k = map(int,input().split())
        locations = [[] for _ in range(k+1)]
        appears = [False]*(k+1)
        uniques = 0
        
        for y in range(n):
            for x,m in enumerate(map(int,input().split())):
                locations[m].append((x,y))
                if not appears[m]:
                    uniques += 1
                    appears[m] = True
        
        return Graph(n,k,locations, uniques == k)

    def __init__(self, n, k, locations, connected):
        self.n = n
        self.k = k
        self.locations = locations
        self.connected = connected

    def shortest(self):
        if not self.connected:
            return -1
        if self.k == 1:
            return 0
        queue = []
        best = [[Graph.INF]*self.n for _ in range(self.n)]
        for x1,y1 in self.locations[self.k]:
            for x2,y2 in self.locations[self.k-1]:
                cost = abs(x1-x2) + abs(y1-y2)
                if best[x2][y2] > cost:
                    heappush(queue, (cost,self.k-1,x2,y2))
                    best[x2][y2] = cost
        return self._djikstra(queue, best)

    def _djikstra(self, queue, best):
        while queue:
            curr_cost, curr_numb, curr_x, curr_y = heappop(queue)
            if curr_numb == 1:
                return curr_cost
            for n_x,n_y in self.locations[curr_numb-1]:
                n_cost = curr_cost + abs(n_x-curr_x) + abs(n_y-curr_y)
                if best[n_x][n_y] > n_cost:
                    heappush(queue, (n_cost, curr_numb-1, n_x, n_y))
                    best[n_x][n_y] = n_cost
        return -1

def main():
    print(Graph.create_from_input().shortest())

if __name__ == "__main__":
    main()