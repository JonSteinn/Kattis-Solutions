variables = {}
while True:
    line = input().split()
    if len(line) == 1:
        if line[0].isdigit():
            if int(line[0]) == 0:
                break
            else:
                print(line[0])
        elif line[0] in variables:
            print(variables[line[0]])
        else:
            print(line[0])
    elif line[1] == '=':
        variables[line[0]] = int(line[2])
    else:
        remaining = []
        s = 0
        for i in enumerate(line):
            if i[0] & 1 != 1:
                if i[1].isdigit():
                    s += int(i[1])
                elif i[1] in variables:
                    s += variables[i[1]]
                else:
                    remaining += [i[1]]
        if s == 0:
            print(' + '.join(remaining))
        else:
            print(' + '.join([str(s)] + remaining))
