class Prime:
    neighbors_cache = {}
    is_prime_cache = {}
    primes = None

    @staticmethod
    def is_prime(n):
        # Assumes n > 24
        if n % 2 == 0 or n % 3 == 0:
            # wont cache these...
            return False
        if n in Prime.is_prime_cache:
            return Prime.is_prime_cache[n]
        i = 5
        while i*i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                Prime.is_prime_cache[n] = False
                return False
            i += 6
        Prime.is_prime_cache[n] = True
        return True

    @staticmethod
    def get_4_digit_primes():
        if Prime.primes is None:
            Prime.primes = {i for i in range(1001, 9974, 2) if Prime.is_prime(i)}
        return Prime.primes

    @staticmethod
    def get_prime_neighbor(p):
        if p not in Prime.neighbors_cache:
            t1 = p // 10 * 10
            n1 = {t1 + i for i in range(1,10,2) if t1+i != p and Prime.is_prime(t1+i)}
            t2 = p // 100 * 100 + p % 10
            n2 = {t2 + i*10 for i in range(10) if t2+i*10 != p and Prime.is_prime(t2+i*10)}
            t3 = p // 1000 * 1000 + p % 100
            n3 = {t3 + i*100 for i in range(10) if t3+i*100 != p and Prime.is_prime(t3+i*100)}
            t4 = p % 1000
            n4 = {t4 + i*1000 for i in range(1,10) if t4+i*1000 != p and Prime.is_prime(t4+i*1000)}
            Prime.neighbors_cache[p] = n1 | n2 | n3 | n4
        return Prime.neighbors_cache[p]

class BFS:
    @staticmethod
    def find_path(a,b):
        return 0 if a==b else BFS.__bfs_search(a,b)

    @staticmethod
    def __bfs_search(a,b):
        visited = {a}
        queue = [(a,0)]
        while queue:
            curr,cost = queue.pop(0)
            if curr == b:
                return cost
            for p in Prime.get_prime_neighbor(curr):
                if p not in visited:
                    visited.add(p)
                    queue.append((p,cost+1))
        return 'Impossible'

def main():
    for _ in range(int(input())):
        print(BFS.find_path(*map(int,input().split())))

if __name__ == "__main__":
    main()