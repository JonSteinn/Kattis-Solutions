def DFS(r,c,i,j,visited,mat):
    stack = [(i,j)]
    while stack:
        cr,cc = stack.pop()
        if (cr,cc) not in visited:
            visited.add((cr,cc))
            if cr-1 >= 0 and mat[cr-1][cc] != 'W':
                stack.append((cr-1,cc))
            if cr+1 < r and mat[cr+1][cc] != 'W':
                stack.append((cr+1,cc))
            if cc-1 >= 0 and mat[cr][cc-1] != 'W':
                stack.append((cr,cc-1))
            if cc+1 < c and mat[cr][cc+1] != 'W':
                stack.append((cr,cc+1))

def main():
    r,c = map(int, input().split())
    mat = [input() for _ in range(r)]
    counter = 0
    visited = set()
    for i,_r in enumerate(mat):
        for j,t in enumerate(_r):
            if t == 'L' and (i,j) not in visited:
                DFS(r,c,i,j,visited,mat)
                counter += 1
    print(counter)

if __name__ == "__main__":
    main()