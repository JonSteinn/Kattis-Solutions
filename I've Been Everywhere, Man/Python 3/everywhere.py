n = int(input())
for i in range(0, n):
    flight_set = {}
    f = int(input())
    for j in range(0, f):
        flight_set[input()] = 1
    print(len(flight_set))