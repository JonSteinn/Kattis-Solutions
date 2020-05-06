from collections import deque

class State(tuple):

    def __new__(cls, *pos):
        return tuple.__new__(cls, *pos)

    def neighbors(self, env):
        for i in range(env.n):
            for n in self._neighbor_of(env, i):
                yield n

    def _neighbor_of(self, env, i):
        r, c = self._get(i)
        
        up = self._travel_up(env, r, c)
        if up != r:
            yield self._change(i, up, c)
        
        down = self._travel_down(env, r, c)
        if down != r:
            yield self._change(i, down, c)

        left = self._travel_left(env, r, c)
        if left != c:
            yield self._change(i, r, left)

        right = self._travel_right(env, r, c)
        if right != c:
            yield self._change(i, r, right)

    def _travel_up(self, env, r, c):
        _r = r
        while _r > 0 and env.world[_r-1][c] != 'W' and not self._contains_player(_r-1, c):
            _r -= 1
        return _r

    def _travel_down(self, env, r, c):
        _r = r
        while _r < env.r-1 and env.world[_r+1][c] != 'W' and not self._contains_player(_r+1, c):
            _r += 1
        return _r

    def _travel_left(self, env, r, c):
        _c = c
        while _c > 0 and env.world[r][_c-1] != 'W' and not self._contains_player(r, _c-1):
            _c -= 1
        return _c

    def _travel_right(self, env, r, c):
        _c = c
        while _c < env.c-1 and env.world[r][_c+1] != 'W' and not self._contains_player(r, _c+1):
            _c += 1
        return _c

    def _get(self, n):
        return self[2*n],self[2*n+1]

    def _contains_player(self, r, c):
        for i in range(0,len(self),2):
            if self[i] == r and self[i+1] == c:
                return True
        return False

    def is_goal_state(self, env):
        return self[0] == env.goal[0] and self[1] == env.goal[1]
    
    def _change(self, i, r, c):
        i *= 2
        return State(self[:i] + (r,c) + self[i+2:])

class Environment:
    @staticmethod
    def create_from_input():
        robots, c, r, limit = map(int, input().split())
        world = [input() for _ in range(r)]
        return Environment(r, c, limit, robots, world)

    def __init__(self, r, c, l, n, world):
        self.r = r
        self.c = c
        self.l = l
        self.n = n
        self.world = world
        self.goal = tuple()

    def find_init_and_goal_state(self):
        lis = [0]*(self.n*2)
        for r in range(self.r):
            for c in range(self.c):
                if self.world[r][c] == 'X':
                    self.goal = (r,c)
                else:
                    val = ord(self.world[r][c])-49
                    if 0 <= val < 4:
                        lis[2*val] = r
                        lis[2*val+1] = c
        return State(lis)

class BFS:
    @staticmethod
    def search(init, env):

        moves = 0
        visited = {init}
        queues = [deque([init]),deque()]

        while True:
            q_i = moves%2
            queue = queues[q_i]
            other = queues[not q_i]
            while queue:
                curr = queues[moves % 2].popleft()
                for neighbor in curr.neighbors(env):
                    if neighbor.is_goal_state(env):
                        return moves + 1
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    other.append(neighbor)
            moves += 1
            if not other or moves >= env.l:
                break

        return 'NO SOLUTION'

def main():
    env = Environment.create_from_input()
    init = env.find_init_and_goal_state()
    print(BFS.search(init, env))

if __name__ == "__main__":
    main()