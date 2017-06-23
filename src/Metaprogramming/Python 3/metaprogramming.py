import sys

variables = {}
cmp = {
    '=': lambda a, b: variables[a] == variables[b],
    '<': lambda a, b: variables[a] < variables[b],
    '>': lambda a, b: variables[a] > variables[b]
}
bool_text = {True: 'true', False: 'false'}

for line in sys.stdin:
    s = line.split()
    if len(s) == 3:
        variables[s[2]] = int(s[1])
    else:
        if s[1] not in variables or s[3] not in variables:
            print('undefined')
        else:
            print(bool_text[cmp[s[2]](s[1], s[3])])