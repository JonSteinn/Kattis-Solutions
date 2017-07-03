def printer(lst, m):
    ind = m - 1
    while ind >= 0 and lst[ind] == ' ':
        ind -= 1
    print("".join(lst[:ind+1]))

first = True
while True:
    n = int(input())
    if n == 0:
        break
    if first:
        first = False
    else:
        print()
    max_width = 0
    mat = []
    for x in range(n):
        lis = list(input())
        if len(lis) > max_width:
            max_width = len(lis)
        mat.append(lis)

    for x in range(n):
        if len(mat[x]) < max_width:
            mat[x] = mat[x] + ([' '] * (max_width - len(mat[x])))

    mat2 = [[' ' for j in range(n)] for i in range(max_width)]
    for x in range(max_width):
        for y in range(n):
            c = mat[y][x]
            if c == '-':
                mat2[x][n - y - 1] = '|'
            elif c == '|':
                mat2[x][n - y - 1] = '-'
            else:
                mat2[x][n - y - 1] = c

    list(map(lambda l: printer(l, n), mat2))