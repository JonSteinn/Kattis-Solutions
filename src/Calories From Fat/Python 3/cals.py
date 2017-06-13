calories_in_grams = [9, 4, 4, 4, 7]


def calories(inp):
    lst = inp.split()
    percentage_sum = 0
    total = 0
    indices = []
    for i in range(len(lst)):
        if lst[i][-1] == 'g':
            lst[i] = float(lst[i][0:-1]) * calories_in_grams[i]
            total += lst[i]
        elif lst[i][-1] == 'C':
            lst[i] = float(lst[i][0:-1])
            total += lst[i]
        else:
            percentage_sum += float(lst[i][0:-1])
            indices += [i]
    total = total / (1 - percentage_sum / 100)
    for i in indices:
        lst[i] = total * float(lst[i][0:-1]) / 100
    return lst


while True:
    s = input()
    if s == '-':
        break
    t = calories(s)
    while True:
        s = input()
        if s == '-':
            break
        t = [sum(x) for x in zip(t, calories(s))]
    print(round(100 * t[0] / sum(t)), end='%\n')