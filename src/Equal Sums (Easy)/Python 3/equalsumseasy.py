def subset_sum(lis, subset):
    s = 0
    i = 0
    while subset > 0:
        if (subset & 1) == 1:
            s += lis[i]
        i += 1
        subset >>= 1
    return s


def subset_as_list(lis, x):
    lst = []
    i = 0
    while x > 0:
        if x&1 == 1:
            lst += [lis[i]]
        i += 1
        x >>= 1
    return lst


def test_case(tc):
    print("Case #{0}:".format(tc))
    lis = list(map(int, input().split()))[1:]
    single = {a: b for b, a in enumerate(lis)}
    ss_map = {}
    for i in range(3, (1 << 20)-1):
        if i & (i-1) != 0:
            sss = subset_sum(lis, i)
            if sss in single:
                print(" ".join(map(str, subset_as_list(lis, i))))
                print(" ".join(map(str, subset_as_list(lis, 1 << single[sss]))))
                return
            elif sss in ss_map:
                print(" ".join(map(str, subset_as_list(lis, ss_map[sss]))))
                print(" ".join(map(str, subset_as_list(lis, i))))
                return
            else:
                ss_map[sss] = i
    print("Impossible")

for t in range(int(input())):
    test_case(t + 1)
