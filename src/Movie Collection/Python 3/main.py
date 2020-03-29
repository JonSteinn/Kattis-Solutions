class FenwickTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.sum_tree = [0] * (self.n + 1)
        for i,x in enumerate(arr):
            self.update(i+1, x) 

    def update(self, i, value):    
        while i <= self.n:
            self.sum_tree[i] += value
            i += i & (-i)
            
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.sum_tree[i]
            i -= i & (-i) 
        return s 

def move_top(x,i,r,ft,index):
    c = ft.sum(index[x]) - 1
    ft.update(index[x], -1)
    index[x] = r - i
    ft.update(index[x], 1)
    return f'{c}'

def test_case(m,r,a):
    ft = FenwickTree([0]*r + [1]*m)
    index = [0]+[r+i+1 for i in range(m)]
    print(' '.join(move_top(x,i,r,ft,index) for i,x in enumerate(a)))

def main(getline = input):
    for _ in range(int(getline())):
        test_case(*map(int, getline().split()), map(int, getline().split()))

if __name__ == "__main__":
    main()

