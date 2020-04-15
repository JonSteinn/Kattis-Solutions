from itertools import islice

def t1(n,data):
    return 7

def t2(n,data):
    a,b = islice(data, 0, 2)
    if a > b:
        return 'Bigger'
    elif a == b:
        return 'Equal'
    else:
        return 'Smaller'

def t3(n,data):
    return sorted(islice(data, 0, 3))[1]

def t4(n,data):
    return sum(data)

def t5(n,data):
    return sum(i for i in data if i%2 == 0)

def t6(n,data):
    return ''.join(chr(97+i % 26) for i in data)

def t7(n,data):
    d = list(data)
    visited = [False]*n
    i = 0
    while True:
        if i >= n:
            return 'Out'
        if visited[i]:
            return 'Cyclic'
        if i == n-1:
            return 'Done'
        visited[i] = True
        i = d[i]

def main():
    n,t = map(int,input().split())
    data = map(int,input().split())
    print([t1,t2,t3,t4,t5,t6,t7][t-1](n,data))

if __name__ == "__main__":
    main()