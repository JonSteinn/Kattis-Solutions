for i in range(int(input())):
    s = input()
    l = len(s)
    for j in range(1, l + 1):
        if s == (s[0:j] * (int(l // j) + 1))[0:l]:
            print(j)
            break