from math import radians, sin, cos, sqrt


def update(p, cmd, val):
    if cmd == 'turn':
        p[2] += val
    else:
        p[0] += val * cos(radians(p[2]))
        p[1] += val * sin(radians(p[2]))


def dist_squared(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def test_case(t):
    pos_coll = []
    x_sum = 0.0
    y_sum = 0.0
    for i in range(t):
        s = input().split()
        pos = list(map(float, s[:2]))
        commands = s[2:]
        it = iter(commands)
        next(it) # dump start
        pos.append(float(next(it)))
        for j in range(len(commands) // 2 - 1):
            update(pos, next(it), float(next(it)))
        pos_coll.append(tuple(pos[:2]))
        x_sum += pos[0]
        y_sum += pos[1]
    average = (x_sum / len(pos_coll), y_sum / len(pos_coll))
    dist = 0
    for p in pos_coll:
        d = dist_squared(p, average)
        if d > dist:
            dist = d
    print("{:.6f} {:.6f} {:.6f}".format(average[0], average[1], sqrt(dist)))


if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        test_case(n)