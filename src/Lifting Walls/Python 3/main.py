def find_cranes_helper(positions, i, n, reach, covered=[False for _ in range(4)]):
    cov = [any((r,s)) for r,s in zip(covered,reach[positions[i]])] 
    if i == n-1:
        return 1 if all(cov) else 5
    else:
        a = 0 + find_cranes_helper(positions, i+1, n, reach, covered)
        b = 1 if all(cov) else 1 + find_cranes_helper(positions, i+1, n, reach, cov)
        return min(a,b)

def find_cranes(positions, reach):
    return find_cranes_helper(positions, 0, len(positions), reach)

def main():
    l,w,n,r = map(int, input().split())#4 2 3 3
    dist_squared_4 = 4*r**2
    within_reach = [
        # Clockwise from left end
        lambda x,y: (2*x+l)**2 + 4*y**2 <= dist_squared_4,
        lambda x,y: 4*x**2 + (2*y-w)**2 <= dist_squared_4,
        lambda x,y: (2*x-l)**2 + 4*y**2 <= dist_squared_4,
        lambda x,y: 4*x**2 + (2*y+w)**2 <= dist_squared_4
    ]
    positions = {}
    for _ in range(n):
        x,y = map(int,input().split())
        reachable = [within_reach[i](x,y) for i in range(4)]
        if any(reachable):
            positions[(x,y)] = reachable
    most_needed = 5 if not positions else find_cranes(sorted(positions.keys(),key=lambda z: -sum(positions[z])),positions)
    if most_needed > 4:
        print('Impossible')
    else:
        print(most_needed)

if __name__ == "__main__":
    main()