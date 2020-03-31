class FenwickTree:
    def __init__(self, n):
        self.arr = [False]*n
        self.n = n
        self.sum_tree = [0] * (self.n + 1)

    def flip(self, i):
        value = -1 if self.arr[i-1] else 1
        self.arr[i-1] = not self.arr[i-1]
        while i <= self.n:
            self.sum_tree[i] += value
            i += i & (-i)

    def sum(self, l, r):
        return self.__single_sum(r) - (self.__single_sum(l-1) if l > 1 else 0)

    def __single_sum(self, i):
        s = 0
        while i > 0:
            s += self.sum_tree[i]
            i -= i & (-i) 
        return s

def main():
    n,k = map(int,input().split())
    ft = FenwickTree(n)
    for _ in range(k):
        inp = input().split()
        if inp[0] == 'F':
            ft.flip(int(inp[1]))
        else:
            print(ft.sum(int(inp[1]),int(inp[2])))

if __name__ == "__main__":
    main()