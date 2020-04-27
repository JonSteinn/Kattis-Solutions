class Binomial:
    MEM = {}
    @staticmethod
    def coef(n,k):
        if n == k or k == 0:
            return 1
        if (n,k) not in Binomial.MEM:
            Binomial.MEM[(n,k)] = Binomial.coef(n-1,k) + Binomial.coef(n-1,k-1)
        return Binomial.MEM[(n,k)]

def main():
    for _ in range(int(input())):
        n,k=map(int,input().split())
        print(f'{Binomial.coef(n,k-1)}')

if __name__ == "__main__":
    main()