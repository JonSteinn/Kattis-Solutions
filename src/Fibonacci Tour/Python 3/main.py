from collections import defaultdict

def gen_all_fibs_less_or_equal_than(n):
    fibs = {}
    a,b,c = 1,1,1
    while True:
        c = a+b
        if c > n:
            break
        fibs[b] = c
        a = b
        b = c
    fibs[b] = None
    return fibs

def filter_vertices(all_fibs):
    V, vertices = 0, {}
    for i,v in enumerate(map(int, input().split())):
        if v in all_fibs:
            vertices[i] = v
            V += 1
    return V,vertices

def filter_edges(m, vertices, all_fibs):
    E,edges,sinks,ones = 0,defaultdict(set),set(vertices.keys()),defaultdict(lambda: [False, set()])
    for _ in range(m):
        u,v = map(int,input().split())
        u,v = u-1,v-1
        if u in vertices and v in vertices:
            a,b = vertices[u], vertices[v]
            if a > b:
                t1,t2 = a,u
                a,u = b,v
                b,v = t1,t2
            if a == b == 1:
                edges[u].add(v)
                edges[v].add(u)
                ones[u][1].add(v)
                ones[v][1].add(u)
                E += 2
            elif b == all_fibs[a]:
                edges[v].add(u)
                sinks.discard(u)
                if a == 1:
                    ones[u][0] = True
                E += 1
    for next_is_not_sink, prevs in ones.values():
        if next_is_not_sink:
            for one in prevs:
                sinks.discard(one)
    return E,edges,sinks

def find_longest_path(V,vertices,E,edges, sinks):
    longest = -1
    visited = set()
    for s in sorted(sinks, key=lambda z: vertices[z], reverse=True):
        stack = [(s,1)]
        while stack:
            curr,d = stack.pop()
            if curr in visited:
                continue
            if vertices[curr] == 1:
                can_reach_another = False
                for w in edges[curr]:
                    if vertices[w] == 1:
                        can_reach_another = True
                        break
                if can_reach_another:
                    longest = max(longest, d+1)
                else:
                    longest = max(longest, d)
            else:
                longest = max(longest, d)
                for w in edges[curr]:
                    stack.append((w,d+1))
            visited.add(curr)
    return longest

def main():
    _,m = map(int,input().split())
    all_fibs = gen_all_fibs_less_or_equal_than(10**18)
    V,vertices = filter_vertices(all_fibs)
    E,edges,sinks = filter_edges(m, vertices, all_fibs)
    
    if V == 0:
        print(0)
    elif V == 1 or E == 0:
        print(1)
    else:
        print(find_longest_path(V,vertices,E,edges,sinks))

if __name__ == "__main__":
    main()