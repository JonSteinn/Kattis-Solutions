from itertools import permutations

class Prime:

    MEM = {}
    
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        if n < 4:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        if n < 25:
            return True
        if n not in Prime.MEM:
            i=5
            while i*i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    Prime.MEM[n] = False
                    return False
                i += 6
            Prime.MEM[n] = True
        return Prime.MEM[n]

def generator(letters, n, primes):
    for i in range(1,n+1):
        for order in permutations(letters, i):
            x = int(''.join(order))
            if Prime.is_prime(x):
                primes.add(x)

def count_primes(letters):
    primes = set()
    generator(letters, len(letters), primes)
    return len(primes)

def main():
    for _ in range(int(input())):
        print(count_primes(list(input())))

if __name__ == "__main__":
    main()