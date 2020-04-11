from collections import deque

class BFS:
    @staticmethod
    def search(init, goal, transitions):
        if init == goal:
            return 0,0
        queue = deque([(init,0)])
        visited = {init}
        best_above = (3601, 0)

        while queue:
            curr, cost = queue.popleft()
            for d in transitions:
                neighbor = min(3600, max(0,curr + d))
                if neighbor == goal:
                    return cost + 1, 0
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append((neighbor, cost+1))
                if neighbor > goal and neighbor < best_above[0]:
                    best_above = (neighbor, cost+1)
        return best_above[1],best_above[0]-goal

def main():
    for _ in range(int(input())):
        _,t = map(int,input().split())
        buttons = set(map(int,input().split()))
        print(*BFS.search(0,t,buttons))

if __name__ == "__main__":
    main()