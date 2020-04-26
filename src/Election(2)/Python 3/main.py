
MSG_WIN = 'GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!'
MSG_LOSE = 'RECOUNT!'
MSG_UNKNOWN = 'PATIENCE, EVERYONE!'

class Binomial:
    SEC_POW = [1] 
    MEM = {}

    @staticmethod
    def pow2(n):
        while len(Binomial.SEC_POW) <= n:
            Binomial.SEC_POW.append(2 * Binomial.SEC_POW[-1])
        return Binomial.SEC_POW[n]


    @staticmethod
    def coef(n,k):
        if n == k or k == 0:
            return 1
        if (n,k) not in Binomial.MEM:
            Binomial.MEM[(n,k)] = Binomial.coef(n-1,k)+Binomial.coef(n-1,k-1)
        return Binomial.MEM[(n,k)]


    @staticmethod
    def binomial_distribution_cdf(n,x):
        return sum(Binomial.coef(n,i) / Binomial.pow2(n) for i in range(x+1))

def test_case(n,v1,v2,w):
    if v1/n > 0.5:
        return MSG_WIN
    if (n-v2)/n <= 0.5:
        return MSG_LOSE
    if 100*(1-Binomial.binomial_distribution_cdf(n-v1-v2, n//2-v1 if n%2 == 0 else int(n/2 - v1))) > w:
        return MSG_WIN
    return MSG_UNKNOWN

def main():
    for _ in range(int(input())):
        print(test_case(*map(int,input().split())))

if __name__ == "__main__":
    main()