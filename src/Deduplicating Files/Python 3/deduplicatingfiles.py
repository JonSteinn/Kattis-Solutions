def xor_hash(s):
    _hash = 0
    for c in s:
        _hash ^= ord(c)
    return _hash

while True:
    n = int(input())
    if n == 0:
        break
    file_sys = {}
    for i in range(0, n):
        line = input()
        _hash = xor_hash(line)
        if _hash not in file_sys:
            file_sys[_hash] = [0, {}]
        file_sys[_hash][0] += 1
        if line not in file_sys[_hash][1]:
            file_sys[_hash][1][line] = 1
        else:
            file_sys[_hash][1][line] += 1
    coll = 0
    files = 0
    for _, val in file_sys.items():
        if val[0] > 1:
            for k, v in val[1].items():
                coll += (val[0] - v) * v
            files += len(val[1])
        else:
            files += 1
    print("{:d} {:d}".format(files, coll//2))