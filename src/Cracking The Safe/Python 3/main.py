from collections import deque

class State(int):
    @staticmethod
    def mat_to_int(mat):
        n = 0
        for r,row in enumerate(mat):
            for c,x in enumerate(row):
                n |= x << ((r*3 + c)<<1)
        return n

    @staticmethod
    def int_to_mat(n):
        mat = []
        for _ in range(3):
            mat.append([(n>>(i<<1)) & 0b11 for i in range(3)])
            n >>= 6
        return mat

    def __new__(cls, mat):
        return int.__new__(cls, State.mat_to_int(mat))

    def push(self,r,c):
        mat = State.int_to_mat(self)
        for _r in range(3):
            mat[_r][c] = (mat[_r][c] + 1)%4
        for _c in range(3):
            if _c != c:
                mat[r][_c] = (mat[r][_c] + 1)%4
        return State(mat)

    def neighbors(self):
        for r in range(3):
            for c in range(3):
                yield self.push(r,c)

    def pushes_needed(self):
        if self == 0:
            return 0
        cost = 1
        curr_queue = False
        queues = [deque([self]),deque()]
        visited = [False] * 262144
        visited[self] = True

        while queues[curr_queue]:
            while queues[curr_queue]:
                curr = queues[curr_queue].popleft()
                for n in curr.neighbors():
                    if not visited[n]:
                        if n == 0:
                            return cost
                        visited[n] = True
                        queues[not curr_queue].append(n)
            cost += 1
            curr_queue = not curr_queue

        return -1

def main():
    src = State([list(map(int,input().split())) for _ in range(3)])
    print(src.pushes_needed())

if __name__ == "__main__":
    main()
