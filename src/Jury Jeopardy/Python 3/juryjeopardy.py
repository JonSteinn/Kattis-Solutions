next_pos = {
    0: lambda p: (p[0] + 1, p[1]),  # E
    1: lambda p: (p[0], p[1] + 1),  # S
    2: lambda p: (p[0] - 1, p[1]),  # W
    3: lambda p: (p[0], p[1] - 1),  # N
}

test_cases = int(input())
print(test_cases)

for tc in range(test_cases):
    pos = {(0, 0)}
    curr_pos = (0, 0)
    curr_or = 0
    max_x = 0
    max_y = 0
    min_y = 0
    for c in input():
        if c == 'L':
            curr_or = (curr_or + 3) % 4
        elif c == 'R':
            curr_or = (curr_or + 1) % 4
        elif c == 'B':
            curr_or = (curr_or + 2) % 4
        curr_pos = next_pos[curr_or](curr_pos)
        pos.add(curr_pos)
        if curr_pos[0] > max_x:
            max_x = curr_pos[0]
        if curr_pos[1] > max_y:
            max_y = curr_pos[1]
        if curr_pos[1] < min_y:
            min_y = curr_pos[1]

    width = max_x + 2
    height = max_y - min_y + 3
    print(height, width)

    for j in range(min_y - 1, max_y + 2):
        line = ['#'] * width
        for i in range(width):
            if (i, j) in pos:
                line[i] = '.'
        print("".join(line))
