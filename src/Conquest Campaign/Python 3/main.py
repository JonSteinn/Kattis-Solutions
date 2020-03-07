
def get_neighbors(x,y,r,c):
    neighbors = []
    if x > 1:
        neighbors.append((x-1,y))
    if y > 1:
        neighbors.append((x,y-1))
    if x < r:
        neighbors.append((x+1,y))
    if y < c:
        neighbors.append((x,y+1))
    return neighbors

def iterations(r, c, occupied):
    n = r*c
    days = 1
    visited = set()
    queue = []
    for a,b in occupied:
        queue.append((a,b,days))
        visited.add((a,b))
    while len(visited) < n:
        x,y,d = queue.pop(0)
        for n_x,n_y in get_neighbors(x,y,r,c):
            if (n_x,n_y) not in visited:
                visited.add((n_x,n_y))
                days = d+1
                queue.append((n_x,n_y,days))
    return days

def main():
    r, c, n = tuple(map(int, input().split()))
    occupied = {tuple(map(int, input().split())) for _ in range(n)}
    print(iterations(r, c, occupied))
    
if __name__ == "__main__":
    main()