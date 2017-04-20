operators = [' + ', ' - ', ' * ', ' // ']

values = {}
for a in operators:
    for b in operators:
        for c in operators:
            val_str = "4{:s}4{:s}4{:s}4".format(a, b, c)
            val = eval(val_str)
            values[val] = val_str.replace('//', '/') + " = {:d}".format(val)

for i in range(0, int(input())):
    n = int(input())
    if n < -60 or n > 256 or n not in values:
        print("no solution")
    else:
        print(values[n])
