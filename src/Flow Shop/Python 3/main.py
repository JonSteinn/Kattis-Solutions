from heapq import heappop, heappush

class P:
    def __init__(self, r, c, t):
        self.r = r
        self.c = c
        self.t = t

    def __lt__(self,other):
        return self.t < other.t

    def decrement(self, t):
        self.t -= t

def get_next(heap):
    ps = [heappop(heap)]
    while heap and heap[0].t == ps[0].t:
        ps.append(heappop(heap))
    for h in heap:
        h.decrement(ps[0].t)
    return ps

def times(r,c,mat):
    time, heap, out = 0, [P(0,0,mat[0][0])], []
    mat[0][0] = 0
    while heap:

        ps = get_next(heap)
        time += ps[0].t

        for p in ps:
            mat[p.r][p.c] = -1
            if p.c == c-1:
                out.append(time)

            neighbors = []
            if p.r < r-1:
                neighbors.append((p.r+1,p.c))
            if p.c < c-1:
                neighbors.append((p.r,p.c+1))
            for n_r,n_c in neighbors:
                if mat[n_r][n_c] > 0 and (n_r == 0 or mat[n_r-1][n_c] == -1) and (n_c == 0 or mat[n_r][n_c-1] == -1):
                    heappush(heap, P(n_r,n_c,mat[n_r][n_c]))
                    mat[n_r][n_c] = 0
    return out

def main():
    r,c = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(r)]
    print(' '.join(str(t) for t in times(r,c,mat)))

if __name__ == "__main__":
    main()