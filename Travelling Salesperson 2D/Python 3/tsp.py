import math

# Will do this properly later...

def distance(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

coordinates = []
n = int(input())
tour = list(range(0,n))
used = {i: False for i in range(0, n)}
used[0] = True

for i in range(0, n):
    coordinates.append((lambda x: (float(x[0]), float(x[1])))(input().split()))

for i in range(1, n):
    best = -1
    for j in range(0, n):
        if not used[j] and (best == -1 or distance(coordinates[tour[i-1]], coordinates[j]) < distance(coordinates[tour[i-1]], coordinates[best])):
            best = j
    tour[i] = best
    used[best] = True

for i in range(0, n):
    print(tour[i])