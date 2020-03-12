class BFS:
    transitions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

    @staticmethod
    def find(start, goal, environment, dim):
        queue = []
        queue.append((start,0))
        visited = {start}
        while queue:
            curr, cost = queue.pop(0)
            if curr == goal:
                return cost
            x,y = curr
            for dx,dy in BFS.transitions:
                nx,ny = (x+dx,y+dy)
                if 0 <= nx < dim and 0 <= ny < dim and environment[nx][ny] != '#' and (nx,ny) not in visited:
                    queue.append(((nx,ny),cost+1))
                    visited.add((nx,ny))
        return -1

def main():
    dim = int(input())
    mat = []
    player = None
    for x in range(dim):
        mat.append(input())
        y = mat[-1].find('K')
        if y != -1:
            player = (x,y)
    print(BFS.find(player, (0,0), mat, dim))

if __name__ == "__main__":
    main()