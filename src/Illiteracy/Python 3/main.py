# Can probably improve this using A* and some heuristic but accepted... so I won't

from collections import deque

class BFS:
    @staticmethod
    def create_from_input():
        return BFS(input(),input())

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    @staticmethod
    def rotate(char):
        return chr(ord('A') + (ord(char)-ord('A')+1)%6)

    @staticmethod
    def _neighbors(s):
        for x,c in enumerate(s):
            if c == 'A':
                yield f'{(s[:x-1] + BFS.rotate(s[x-1]) if x>0 else "")}A{(BFS.rotate(s[x+1]) + s[x+2:] if x<len(s)-1 else "")}'
            elif c == 'B':
                if 0 < x < len(s)-1:
                    yield f'{s[:x+1]}{s[x-1]}{s[x+2:]}'
            elif c == 'C':
                y = 7-x
                yield f'{s[:y]}{BFS.rotate(s[y])}{s[y+1:]}'
            elif c == 'D':
                if 0 < x < len(s)-1:
                    if x < 4:
                        yield f'{"".join(BFS.rotate(z) for z in s[:x])}{s[x:]}'
                    else:
                        yield f'{s[:x+1]}{"".join(BFS.rotate(z) for z in s[x+1:])}'
            elif c == 'E':
                if 0 < x < len(s)-1:
                    y = x if x < 4 else len(s)-1-x
                    yield f'{s[:x-y]}{BFS.rotate(s[x-y])}{s[x-y+1:x+y]}{BFS.rotate(s[x+y])}{s[x+y+1:]}'
            else:
                y = (x+(-1 if x&1 else 8))//2
                yield f'{s[:y]}{BFS.rotate(s[y])}{s[y+1:]}'
                    

    def path_length(self):
        if self.src == self.dst:
            return 0
        
        c = 1
        visited = {self.src}
        curr_queue = False
        queues = (deque([self.src]), deque())

        while queues[curr_queue]:
            while queues[curr_queue]:
                curr = queues[curr_queue].popleft()
                for neighbor in BFS._neighbors(curr):
                    if neighbor not in visited:
                        if neighbor == self.dst:
                            return c
                        visited.add(neighbor)
                        queues[not curr_queue].append(neighbor)
            c += 1
            curr_queue = not curr_queue

def main():
    print(BFS.create_from_input().path_length())

if __name__ == "__main__":
    main()