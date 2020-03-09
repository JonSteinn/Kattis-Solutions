from heapq import heappop, heappush
from collections import defaultdict

intersections, streets = tuple(map(int, input().split()))
start, goal, delay, number_visited_by_george = tuple(map(int, input().split()))
order_visited_by_george = list(map(int, input().split()))

transitions = defaultdict(lambda: {})
for _ in range(streets):
    i1, i2, dist = tuple(map(int, input().split()))
    transitions[i1][i2] = dist
    transitions[i2][i1] = dist

blocked = defaultdict(lambda: (0,0))
last_d = 0
for i in range(number_visited_by_george-1):
    d = transitions[order_visited_by_george[i]][order_visited_by_george[i+1]]
    blocked[(order_visited_by_george[i], order_visited_by_george[i+1])] = (last_d-delay,last_d + d-delay)
    blocked[(order_visited_by_george[i+1], order_visited_by_george[i])] = (last_d-delay,last_d + d-delay)
    last_d += d 

closed_set = set()
open_set = []
heappush(open_set, (0, start))

while open_set:
    dist, current = heappop(open_set)
    closed_set.add(current)

    if current == goal:
        print(dist)
        break

    for neighbor, d in transitions[current].items():
        if neighbor in closed_set:
            continue
        a,b = blocked[(current, neighbor)]
        if b != 0 and a <= dist < b:
            heappush(open_set, (b + d, neighbor))
        else:
            heappush(open_set, (d + dist, neighbor))