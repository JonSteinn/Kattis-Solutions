n, q = map(int, input().split())

d = "0"
vals = {}


for _ in range(q):
    inp = input()
    if inp[0] == "S":
        _, a, b = inp.split()
        vals[a] = b
    elif inp[0] == "P":
        print(vals.get(inp.split()[1], d))
    else:
        vals.clear()
        d = inp.split()[1]