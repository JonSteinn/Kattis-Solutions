from heapq import heappop, heappush

def djikstra(adj, src, dst):
    open_set,closed_set = [(-1,src)],[False]*len(adj)
    while open_set:
        f, v = heappop(open_set)
        if v == dst:
            return -f
        closed_set[v] = True
        for u,w in adj[v]:
            if not closed_set[u]:
                heappush(open_set,(f*w, u))

def main():
    while True:
        n,m = map(int,input().split())
        if n + m == 0:
            break
        adj = [[] for _ in range(n)]
        for _ in range(m):
            *verties,w = input().split()
            u,v = map(int,verties)
            w = float(w)
            adj[u].append((v,w))
            adj[v].append((u,w))
        print('%.4f' % djikstra(adj,0,n-1))

if __name__ == "__main__":
    main()