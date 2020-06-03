from heapq import heappop, heappush

class Graph:
    INF = 2500000000

    def __init__(self, v, roads, flights):
        self.v = v
        self.roads = [[] for _ in range(v)]
        self.flights = [[] for _ in range(v)]
        for a,b,w in roads:
            self.roads[a].append((b,w))
            self.roads[b].append((a,w))
        for a,b in flights:
            self.flights[a].append(b)

    def shortest_path(self, src, dst):
        # Setup
        dist = [[Graph.INF]*self.v for _ in range(2)]
        dist[False][src] = 0
        dist[True][src] = 0
        pq = [(0,src,False)]

        while pq:
            # Extract next
            cost,curr,used = heappop(pq)

            # Goal check
            if curr == dst:
                return cost

            # Travel by roads
            for neighbor, w in self.roads[curr]:
                new_cost = cost + w
                if new_cost < dist[used][neighbor]:
                    dist[used][neighbor] = new_cost
                    heappush(pq, (new_cost, neighbor, used))
            
            # If not already used, travel by flight
            if not used:
                for neighbor in self.flights[curr]:
                    if cost < dist[True][neighbor]:
                        dist[True][neighbor] = cost
                        heappush(pq, (cost, neighbor, True))
        
        return -1

def get_input():
    v,e,f,src,dst = map(int,input().split())
    roads = (map(int,input().split()) for _ in range(e))
    flights = (map(int,input().split()) for _ in range(f))
    return v,src,dst,roads,flights

def main():
    v,src,dst,roads,flights = get_input()
    g = Graph(v,roads,flights)
    print(g.shortest_path(src,dst))

if __name__ == "__main__":
    main()