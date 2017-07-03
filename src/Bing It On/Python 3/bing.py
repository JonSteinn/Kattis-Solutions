d = {'W': int(input())}

for i in range(d['W']):
    c_d = d
    val = 0
    for j in input():
        if j not in c_d:
            c_d[j] = {'W': 1}
        c_d = c_d[j]
        c_d['W'] = c_d['W'] + 1
        val = c_d['W']
    print(val - 2)
