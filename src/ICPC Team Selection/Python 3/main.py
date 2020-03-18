from collections import deque

def best_median(d):
    s = 0
    while d:
        d.pop()
        s += d.pop()
        d.popleft()
    return s

def main():
    for _ in range(int(input())):
        input()
        print(best_median(deque(sorted(map(int, input().split())))))

if __name__ == "__main__":
    main()