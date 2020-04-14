def shuffle(lis, split_func):
    first, second = split_func(lis)
    res = []
    for a,b in zip(first,second):
        res.append(a)
        res.append(b)
    if len(first) != len(second):
        res.append(first[-1])
    return res

def shuffler(lis, split_func):
    c = 0
    curr = lis
    while True:
        curr = shuffle(curr, split_func)
        c += 1
        if curr == lis:
            return c

def shuffle_out(n):
    return shuffler(list(range(n)), lambda l: (l[:(len(l)+1)//2],l[(len(l)+1)//2:]))

def shuffle_in(n):
    return shuffler(list(range(n)), lambda l: (l[len(l)//2:],l[:len(l)//2]))

def main():
    n, t = input().split()
    print(shuffle_out(int(n)) if t[0] == 'o' else shuffle_in(int(n)))

if __name__ == "__main__":
    main()