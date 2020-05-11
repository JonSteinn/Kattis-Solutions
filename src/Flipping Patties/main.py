from collections import deque

def main():
    time = deque([0]*43201)
    for _ in range(int(input())):
        d,t = map(int,input().split())
        time[t] += 1
        time[t-d] += 1
        time[t-2*d] += 1
    cooks = -1
    while time:
        cooks = max(cooks, (lambda z: (z+1)//2 if z&1 else z//2)(time.pop()))
    print(cooks)

if __name__ == "__main__":
    main()