def experiment(segments):
    if segments < 2:
        input()
        return 0
    red = []
    blue = []
    for seg in input().split():
        if seg[-1] == 'B':
            blue.append(int(seg[:-1]))
        else:
            red.append(int(seg[:-1]))
    usable = min(len(red), len(blue))
    if usable == 0:
        return 0
    total = 0
    red.sort(reverse=True)
    blue.sort(reverse=True)
    for i in range(0, usable):
        total += red[i] + blue[i]
    total -= usable << 1
    return total


for i in range(0, int(input())):
    print("Case #{:d}: {:d}".format(i + 1, experiment(int(input()))))
