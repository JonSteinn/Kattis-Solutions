import sys

d = {}
v = {}
for line in sys.stdin:
    s = line.split()
    if s[0] == 'def':
        if s[1] in d.keys():
            del v[int(d[s[1]])]
        d[s[1]] = s[2]
        v[int(s[2])] = s[1]
    elif s[0] == 'calc':
        if len(list(filter(lambda z: z in d.keys(), s[1:][::2]))) != len(s[1:][::2]):
            print(" ".join(s[1:]), 'unknown')
        else:
            val = eval(" ".join(map(lambda z: d[z] if z in d.keys() else z, s[1:-1])))
            if val in v.keys():
                print(" ".join (s[1:]), v[val])
            else:
                print(" ".join (s[1:]), 'unknown')
    else:
        d.clear()
        v.clear()