from collections import deque

class Peg:
    INVALIDS = {
        (0,0),(0,1),(0,2),(0,6),(0,7),(0,8),
        (4,0),(4,1),(4,2),(4,6),(4,7),(4,8),
        (-1,3),(-1,4),(-1,5),
        (5,3),(5,4),(5,5),
        (1,-1),(2,-1),(3,-1),
        (1,9),(2,9),(3,9)
    }
    
    INF = 100

    @staticmethod
    def moves(pins):
        visited = {frozenset(pins)}
        queue = deque()
        queue.append((0,pins))
        return Peg.__bfs(visited, queue)

    @staticmethod
    def __bfs(visited, queue):
        best_left, best_moves = (Peg.INF,)*2
        while queue:
            cost, pins = queue.popleft()
            if len(pins) < best_left or (best_left == len(pins) and cost < best_moves):
                best_left = len(pins)
                best_moves = cost
            for p in Peg.__neighbors(pins):
                if p not in visited:
                    if len(p) < 2:
                        return len(p), cost + 1
                    visited.add(frozenset(p))
                    queue.append((cost+1, p))
        return best_left, best_moves

    @staticmethod
    def __neighbors(pins):
        for r,c in pins:
            if (r-1,c) in pins and (r-2,c) not in pins and (r-2,c) not in Peg.INVALIDS:
                tmp =  pins - {(r-1,c),(r,c)}
                tmp.add((r-2,c))
                yield tmp
            if (r+1,c) in pins and (r+2,c) not in pins and (r+2,c) not in Peg.INVALIDS:
                tmp =  pins - {(r+1,c),(r,c)}
                tmp.add((r+2,c))
                yield tmp
            if (r,c-1) in pins and (r,c-2) not in pins and (r,c-2) not in Peg.INVALIDS:
                tmp = pins - {(r,c-1),(r,c)}
                tmp.add((r,c-2))
                yield tmp
            if (r,c+1) in pins and (r,c+2) not in pins and (r,c+2) not in Peg.INVALIDS:
                tmp = pins - {(r,c+1),(r,c)}
                tmp.add((r,c+2))
                yield tmp

def main():
    for i in range(int(input())):
        if i != 0:
            input() # Dump empty line
        pins = {(r,c) for r in range(5) for c,x in enumerate(input()) if x == 'o'}
        print(*Peg.moves(pins))

if __name__ == "__main__":
    main()