def read():
    s,t,n = map(int,input().split())
    walks = list(map(int, input().split()))
    drives = list(map(int, input().split()))
    arrivals = list(map(int, input().split()))
    return s,t,n,walks,drives,arrivals

def on_time(s,t,n,walks,drives,arrivals):
    for _ in range(n):
        s += walks.pop(0)
        s += (lambda a: (a-(s%a))%a)(arrivals.pop(0))
        s += drives.pop(0)
        if s > t:
            return False
    return s + walks.pop() <= t

def main():
    print('yes' if on_time(*read()) else 'no')

if __name__ == "__main__":
    main()