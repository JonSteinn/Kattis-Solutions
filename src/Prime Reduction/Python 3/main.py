from math import sqrt
from collections import Counter, deque


class Prime:
    MAX = 1_000_000_000
    SQ_MAX = 31623
    DIV_PRIMES = []
    REDUCTION_MEM = {}

    @staticmethod
    def init():
        Prime.DIV_PRIMES = Prime.soe(Prime.SQ_MAX)

    @staticmethod
    def soe(n):
        prime_list, is_prime, x, top = [], [True for i in range(n + 1)], 2, sqrt(n)
        while x <= top: 
            if is_prime[x] == True:
                prime_list.append(x)
                for f in range(2,n//x+1): 
                    is_prime[f*x] = False
            x += 1
        while x <= n:
            if is_prime[x]: 
                prime_list.append(x)
            x += 1
        return prime_list
    
    @staticmethod
    def factor(n):
        ncopy, top = n, sqrt(n)
        p_factors = Counter()
        for p in Prime.DIV_PRIMES:
            if p > top or n == 1:
                break
            while n > 1:
                d,m = divmod(n, p)
                if m == 0:
                    p_factors[p] += 1
                    n = d
                else:
                    break
        if n > 1:
            p_factors[n] += 1
        if p_factors:
            return p_factors
        else:
            return Counter({ncopy: 1})

    @staticmethod
    def reduction(n):
        stack = deque([n])
        c = 1
        while True:
            if stack[0] in Prime.REDUCTION_MEM:
                last, c = Prime.REDUCTION_MEM[stack[0]]
                c += 1
                stack.popleft()
                break
            stack.appendleft(sum(a*b for a,b in Prime.factor(stack[0]).items()))
            if stack[0] == stack[1]:
                last = stack.popleft()
                break
        while stack:
            Prime.REDUCTION_MEM[stack.popleft()] = (last,c)
            c += 1
        return Prime.REDUCTION_MEM[n]

def main():
    Prime.init()
    while True:
        n = int(input())
        if n == 4:
            break
        print(*Prime.reduction(n))

if __name__ == "__main__":
    main()