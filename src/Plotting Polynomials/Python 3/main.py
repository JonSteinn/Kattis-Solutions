class Binomial:
    mem = [[1]]

    @staticmethod
    def coefficient(n,k):
        while len(Binomial.mem) <= n:
            Binomial.mem.append([1] + [a+b for a,b in zip(Binomial.mem[-1],Binomial.mem[-1][1:])] + [1])
        return Binomial.mem[n][k]

class Polynomial:
    def __init__(self,a,n):
        self.a = a
        self.points = [self._eval_at(x) for x in range(n+1)]

    def _eval_at(self,x):
        return self.a[0] if x==0 else sum(a*x**i for i,a in enumerate(self.a))

    def __getitem__(self,x):
        return self.points[x]

def find_c(n,a):
    p = Polynomial(a,n)
    c = [p[0]]
    for i in range(n):
        c.append(p[i+1]-p[i] - sum(Binomial.coefficient(i,j)*_c for j,_c in enumerate(c[1:])))
    return c

def main():
    n,*a = map(int,input().split())
    print(*find_c(n,a[::-1]))

if __name__ == "__main__":
    main()