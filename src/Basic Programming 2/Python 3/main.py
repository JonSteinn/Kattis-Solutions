from collections import Counter

def t1(n,arr):
    s=set(arr)
    for i in range(1,7777):
        if i in s and 7777-i in s:
            return ('Yes',)
    return ('No',)

def t2(n,arr):
    return ('Unique',) if len(set(arr))==n else ('Contains duplicate',)

def t3(n,arr):
    a,b = Counter(arr).most_common(1)[0]
    return (a,) if b > n/2 else (-1,)

def t4(n,arr):
    s = sorted(arr)
    if len(s)%2 == 1:
        return (s[len(s)//2],)
    else:
        return s[len(s)//2 - 1: len(s)//2 + 1]

def t5(n,arr):
    return sorted(filter(lambda z: 99 < z < 1000, arr))

def action(n,t,arr):
    return [t1,t2,t3,t4,t5][t-1](n,arr)

def main():
    print(*action(*map(int,input().split()),map(int,input().split())))

if __name__ == "__main__":
    main()