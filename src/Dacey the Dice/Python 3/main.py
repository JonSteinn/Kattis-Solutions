from collections import deque

class Node(tuple):
    #####   ^ -- backwad
    #####   v -- forward
    #####   <-- left
    #####   --> right
    LEFT,RIGHT,TOP,BOTTOM,FORWARD,BACKWARD = range(6)

    def __new__(cls, r, c, five):
        return tuple.__new__(cls, (r,c,five))

    def __init__(self, r, c, five):
        pass

    def neighbors(self, mat, n):
        r,c,_ = self
        if r > 0 and mat[r-1][c] != '*':
            yield self.roll_backwards()
        if c > 0 and mat[r][c-1] != '*':
            yield self.roll_left()
        if r < n-1 and mat[r+1][c] != '*':
            yield self.roll_forward()
        if c < n-1 and mat[r][c+1] != '*':
            yield self.roll_right()

    def roll_forward(self):
        r,c,five = self
        if five == Node.FORWARD:
            five = Node.BOTTOM
        elif five == Node.BOTTOM:
            five = Node.BACKWARD
        elif five == Node.BACKWARD:
            five = Node.TOP
        elif five == Node.TOP:
            five = Node.FORWARD
        return Node(r+1, c, five)

    def roll_backwards(self):
        r,c,five = self
        if five == Node.FORWARD:
            five = Node.TOP
        elif five == Node.BOTTOM:
            five = Node.FORWARD
        elif five == Node.BACKWARD:
            five = Node.BOTTOM
        elif five == Node.TOP:
            five = Node.BACKWARD
        return Node(r-1, c, five)

    def roll_left(self):
        r,c,five = self
        if five == Node.LEFT:
            five = Node.BOTTOM
        elif five == Node.BOTTOM:
            five = Node.RIGHT
        elif five == Node.RIGHT:
            five = Node.TOP
        elif five == Node.TOP:
            five = Node.LEFT
        return Node(r, c-1, five)

    def roll_right(self):
        r,c,five = self
        if five == Node.LEFT:
            five = Node.TOP
        elif five == Node.BOTTOM:
            five = Node.LEFT
        elif five == Node.RIGHT:
            five = Node.BOTTOM
        elif five == Node.TOP:
            five = Node.RIGHT
        return Node(r, c+1, five)

def find_ends(mat):
    start, end = None, None
    for r, row in enumerate(mat):
        for c, x in enumerate(row):
            if x == 'S':
                start = Node(r,c,Node.LEFT)
                if end:
                    return start,end
            elif x == 'H':
                end = Node(r,c,Node.BOTTOM)
                if start:
                    return start, end

def dfs(mat,n,start,end):
    stack = deque()
    stack.append(start)
    visited = {start}
    while stack:
        curr = stack.pop()
        if curr == end:
            return True
        for neighbor in curr.neighbors(mat,n):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return False

def main():
    for _ in range(int(input())):
        n = int(input())
        mat = [input() for _ in range(n)]
        start,end = find_ends(mat)
        print('Yes' if dfs(mat,n,start,end) else 'No')

if __name__ == "__main__":
    main()