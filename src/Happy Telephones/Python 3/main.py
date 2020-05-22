class Interval(tuple):
    def __new__(cls, a, b):
        return tuple.__new__(cls,(a,a+b))

    def intersects(self, other):
        return any((
            self[0] <= other[0] < self[1],
            self[0] < other[1] <= self[1],
            other[0] < self[0] and other[1] > self[1]
        ))

def main():
    while True:
        n,m = map(int,input().split())
        if n == m == 0:
            break
        intervals = [Interval(*map(int,input().split()[2:])) for _ in range(n)]
        for _ in range(m):
            iv = Interval(*map(int,input().split()))
            print(sum(iv.intersects(i) for i in intervals))

if __name__ == "__main__":
    main()