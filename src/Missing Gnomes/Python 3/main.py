from collections import deque

def print_perm(rest,order):
    while rest and order:
        r_next = rest.popleft()
        o_next = order.popleft()
        if r_next < o_next:
            print(r_next)
            order.appendleft(o_next)
        else:
            print(o_next)
            rest.appendleft(r_next)
    for x in rest:
        print(x)
    for x in order:
        print(x)

def main():
    n,m = map(int,input().split())
    rest, order = deque(), deque()
    visited = set()
    for _ in range(m):
        order.append(int(input()))
        visited.add(order[-1])
    for i in range(n):
        if i+1 not in visited:
            rest.append(i+1)
    print_perm(rest,order)

if __name__ == "__main__":
    main()