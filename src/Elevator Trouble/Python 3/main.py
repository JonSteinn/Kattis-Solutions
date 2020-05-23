from collections import deque

def bfs(f,s,g,u,d):
    if s == g:
        return 0
    visited = [False] * f
    visited[s-1] = True
    curr_queue = False
    queues = [deque([s]),deque()]
    cost = 1

    while queues[curr_queue]:
        while queues[curr_queue]:
            curr = queues[curr_queue].popleft()
            up,down = curr+u,curr-d
            if up == g or down == g:
                return cost
            if up <= f and not visited[up-1]:
                queues[not curr_queue].append(up)
                visited[up-1] = True
            if down > 0 and not visited[down-1]:
                queues[not curr_queue].append(down)
                visited[down-1] = True
            
        cost += 1
        curr_queue = not curr_queue

    return 'use the stairs'

def main():
    print(bfs(*map(int,input().split())))

if __name__ == "__main__":
    main()