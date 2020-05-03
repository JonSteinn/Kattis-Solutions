from collections import deque

class Graph:
    def __init__(self, r, c, mat):
        self.r = r
        self.c = c
        self.mat = mat
        self.visited = [[False]*c for _ in range(r)]
        self.fire_queue, self.joe_queue = self._find_init()

    def _find_init(self):
        f,j = deque(), deque()
        for _r in range(self.r):
            for _c in range(self.c):
                if self.mat[_r][_c] == 'F':
                    f.append((_r,_c))
                    self.visited[_r][_c] = True
                elif self.mat[_r][_c] == 'J':
                    j.append((_r,_c))
                    self.visited[_r][_c] = True
        return f,j

    def search(self):
        if 0 == self.joe_queue[0][0] or self.joe_queue[0][0] == self.r-1 or 0 == self.joe_queue[0][1] or self.joe_queue[0][1] == self.c-1:
            return 1

        rounds = 1
        while self.joe_queue:
            rounds += 1
            self._sim_one_round_fire()
            if self._sim_one_round_joe():
                return rounds
        return -1

    def _sim_one_round_fire(self):
        tmp_queue = deque()

        while self.fire_queue:
            c_r,c_c = self.fire_queue.popleft()
            if c_r > 0 and not self.visited[c_r-1][c_c] and self.mat[c_r-1][c_c] != '#':
                self.visited[c_r-1][c_c] = True
                tmp_queue.append((c_r-1,c_c))
            if c_r < self.r-1 and not self.visited[c_r+1][c_c] and self.mat[c_r+1][c_c] != '#':
                self.visited[c_r+1][c_c] = True
                tmp_queue.append((c_r+1,c_c))
            if c_c > 0 and not self.visited[c_r][c_c-1] and self.mat[c_r][c_c-1] != '#':
                self.visited[c_r][c_c-1] = True
                tmp_queue.append((c_r,c_c-1))
            if c_c < self.c-1 and not self.visited[c_r][c_c+1] and self.mat[c_r][c_c+1] != '#':
                self.visited[c_r][c_c+1] = True
                tmp_queue.append((c_r,c_c+1))

        self.fire_queue = tmp_queue


    def _sim_one_round_joe(self):
        tmp_queue = deque()

        while self.joe_queue:
            c_r,c_c = self.joe_queue.popleft()
            if c_r > 0 and not self.visited[c_r-1][c_c] and self.mat[c_r-1][c_c] == '.':
                if c_r - 1 == 0:
                    return True
                self.visited[c_r-1][c_c] = True
                tmp_queue.append((c_r-1,c_c))
            if c_r < self.r-1 and not self.visited[c_r+1][c_c] and self.mat[c_r+1][c_c] == '.':
                if c_r + 1 == self.r - 1:
                    return True
                self.visited[c_r+1][c_c] = True
                tmp_queue.append((c_r+1,c_c))
            if c_c > 0 and not self.visited[c_r][c_c-1] and self.mat[c_r][c_c-1] == '.':
                if c_c - 1 == 0:
                    return True
                self.visited[c_r][c_c-1] = True
                tmp_queue.append((c_r,c_c-1))
            if c_c < self.c-1 and not self.visited[c_r][c_c+1] and self.mat[c_r][c_c+1] == '.':
                if c_c + 1 == self.c - 1:
                    return True
                self.visited[c_r][c_c+1] = True
                tmp_queue.append((c_r,c_c+1))

        self.joe_queue = tmp_queue
        return False


def main():
    r,c = map(int,input().split())
    mat = [input() for _ in range(r)]
    g = Graph(r,c,mat)
    shortest = g.search()
    print('IMPOSSIBLE' if shortest == -1 else shortest)

if __name__ == "__main__":
    main()