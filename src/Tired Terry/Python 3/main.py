from itertools import islice

def can_wake(p,d,pattern):
    sleeps = 0
    for x in islice(pattern,0,p):
        if x == 'Z':
            sleeps += 1
    not_tired = 1 if sleeps >= d else 0
    for i,x in enumerate(islice(pattern,p,None)):
        if pattern[i] == 'Z':
            sleeps -= 1
        if x == 'Z':
            sleeps += 1
        if sleeps >= d:
            not_tired +=1
    return not_tired 

def tired(n,p,d,pattern):
    if p == 1:
        return pattern.count('W')
    return n-can_wake(p,d,pattern)

def main():
    n,p,d = map(int,input().split())
    pattern = (lambda w: w + w[:p-1])(input())
    print(tired(n,p,d,pattern))

if __name__ == "__main__":
    main()