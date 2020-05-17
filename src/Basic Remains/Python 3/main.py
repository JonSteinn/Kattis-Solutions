from collections import deque

def to_base(b, n):
    d = deque()
    while n:
        d.appendleft(str(n%b))
        n //= b
    while len(d) > 1 and d[0] == '0':
        d.popleft()
    if not d:
        d.appendleft('0')
    return ''.join(d)

def main():
    while True:
        inp = input()
        if inp == '0':
            break
        b,p,m = (lambda _b,_p,_m: (int(_b),_p,_m))(*inp.split())
        print(to_base(b,int(p,base=b)%int(m,base=b)))

if __name__ == "__main__":
    main()