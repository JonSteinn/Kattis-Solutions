from collections import deque

class Node:
    def __init__(self, r, c, cost=1):
        self.r = r
        self.c = c
        self.cost = cost

    def neighbors(self, r, c, mat):
        for _r in range(self.r+1, r):
            if mat[_r][self.c] == '.':
                continue
            if mat[_r][self.c] == 'T':
                yield Node(_r,self.c,self.cost+1)
            break
        for _r in range(self.r-1,-1,-1):
            if mat[_r][self.c] == '.':
                continue
            if mat[_r][self.c] == 'T':
                yield Node(_r,self.c,self.cost+1)
            break
        for _c in range(self.c+1,c):
            if mat[_r][self.c] == '.':
                continue
            if mat[self.r][_c] == 'T':
                yield Node(self.r,_c,self.cost+1)
            break
        for _c in range(self.c-1,-1,-1):
            if mat[_r][self.c] == '.':
                continue
            if mat[self.r][_c] == 'T':
                yield Node(self.r,_c,self.cost+1)
            break

    def __str__(self):
        return f'({self.r},{self.c})'

    def __repr__(self):
        return self.__str__()

def init_top_bt(mat,r,c,queue):
    for _c in range(c):
        for _r in range(r):
            if mat[_r][_c] == '.':
                continue
            if mat[_r][_c] == 'T':
                mat[_r][_c] = '1'
                queue.append(Node(_r,_c))
            break
        for _r in range(r-1,-1,-1):
            if mat[_r][_c] == '.':
                continue
            if mat[_r][_c] == 'T':
                mat[_r][_c] = '1'
                queue.append(Node(_r,_c))
            break

def init_sides(mat,r,c,queue):    
    for _r in range(r):
        for _c in range(c):
            if mat[_r][_c] == '.':
                continue
            if mat[_r][_c] == 'T':
                mat[_r][_c] = '1'
                queue.append(Node(_r,_c))
            break
        for _c in range(c-1,-1,-1):
            if mat[_r][_c] == '.':
                continue
            if mat[_r][_c] == 'T':
                mat[_r][_c] = '1'
                queue.append(Node(_r,_c))
            break

# DFS
def find_init(mat, r, c):
    init = set()
    stack = deque()
    for _r in range(r):
        for _c in range(c):
            if mat[_r][_c] == '.' or _r == 0 or _r == r-1 or _c == 0 or _c == c-1:
                stack.append((_r,_c))
    visited = [[False] * c for _ in range(r)]
    while stack:
        _r,_c = stack.pop()
        if mat[_r][_c] == 'T':
            init.add((_r,_c))
        elif mat[_r][_c] == '.' and not visited[_r][_c]:
            visited[_r][_c] = True
            if _c > 0 and not visited[_r][_c-1]:
                stack.append((_r,_c-1))
            if _c < c-1 and not visited[_r][_c+1]:
                stack.append((_r,_c+1))
            if _r > 0 and not visited[_r-1][_c]:
                stack.append((_r-1,_c))
            if _r < r-1 and not visited[_r+1][_c]:
                stack.append((_r+1,_c))
    queue = deque()
    for _r,_c in init:
        mat[_r][_c] = '1'
        queue.append(Node(_r,_c,1))
    return queue

# BFS
def simulate(mat, r, c):
    longest = 1
    queue = find_init(mat,r,c)
    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors(r,c,mat):
            if mat[neighbor.r][neighbor.c] == 'T':
                queue.append(neighbor)
                mat[neighbor.r][neighbor.c] = str(neighbor.cost)
                longest = max(longest, len(mat[neighbor.r][neighbor.c]))
    return longest

def format_strings(mat, r, c, longest):
    for _c in range(c):
        for _r in range(r):
            mat[_r][_c] = '.' * (longest-len(mat[_r][_c])+1) + mat[_r][_c]

def main():
    r,c = map(int,input().split())
    mat = [list(input()) for _ in range(r)]
    longest = simulate(mat, r, c)
    format_strings(mat,r,c, longest)
    print('\n'.join((''.join(row) for row in mat)))

if __name__ == "__main__":
    main()