from collections import defaultdict,deque

def split_in_two(v, vertices, edges):
    split = [set(), set()]
    stack = deque()

    for u in range(v):
        if any(u in s for s in split):
            continue
        stack.append((len(split[0]) > len(split[1]) , u))
        while stack:
            i,w = stack.pop()
            if w in split[not i]:
                print('impossible')
                return
            if w in split[i]:
                continue
            split[i].add(w)
            for z in edges[w]:
                stack.append((not i, z))
    
    for s in split:
        print(*(vertices[u] for u in s))
    
def main():
    v = int(input())
    vertices = [input().rstrip() for _ in range(v)]
    v_map = {v:i for i,v in enumerate(vertices)}
    e = int(input())
    edges = defaultdict(set)
    for _ in range(e):
        u1,u2 = map(lambda z: v_map[z], input().split())
        edges[u1].add(u2)
        edges[u2].add(u1)
    split_in_two(v, vertices, edges)

if __name__ == "__main__":
    main()