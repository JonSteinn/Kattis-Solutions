from collections import deque

def collect_all(n, pending, to_collect):
    most = 0
    visited = set()
    while pending and to_collect:
        cost,curr_r,curr_c = pending.popleft()
        visited.add((curr_r,curr_c))

        if curr_r > 0 and (curr_r-1,curr_c) not in visited:
            visited.add((curr_r-1,curr_c))
            pending.append((cost+1,curr_r-1,curr_c))
            if (curr_r-1,curr_c) in to_collect:
                most = max(most, cost + 1)
                to_collect.discard((curr_r-1,curr_c))
    
        if curr_r < n-1 and (curr_r+1,curr_c) not in visited:
            visited.add((curr_r+1,curr_c))
            pending.append((cost+1,curr_r+1,curr_c))
            if (curr_r+1,curr_c) in to_collect:
                most = max(most, cost + 1)
                to_collect.discard((curr_r+1,curr_c))

        if curr_c > 0 and (curr_r,curr_c-1) not in visited:
            visited.add((curr_r,curr_c-1))
            pending.append((cost+1,curr_r,curr_c-1))
            if (curr_r,curr_c-1) in to_collect:
                most = max(most, cost + 1)
                to_collect.discard((curr_r,curr_c-1))

        if curr_c < n-1 and (curr_r,curr_c+1) not in visited:
            visited.add((curr_r,curr_c+1))
            pending.append((cost+1,curr_r,curr_c+1))
            if (curr_r,curr_c+1) in to_collect:
                most = max(most, cost + 1)
                to_collect.discard((curr_r,curr_c+1))
    
    return most

def main():
    n = int(input())
    starts, goals = deque(), set()
    for r in range(n):
        for c,x in enumerate(input()):
            if x == 'H':
                starts.append((0,r,c,))
            elif x == 'S':
                goals.add((r,c))
    print(collect_all(n, starts, goals))

if __name__ == "__main__":
    main()