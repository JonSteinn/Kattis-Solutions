class Fibonacci:
    MOD = 10**9+7

    @staticmethod
    def _helper(n):
        if n == 0:
            return (0, 1)
        else:
            c, d, _d = (lambda a,b: (a * (b * 2 - a), *(lambda z: (z, z % Fibonacci.MOD))(a * a + b * b)))(*Fibonacci._helper(n // 2))
            if n % 2 == 0:
                return (c % Fibonacci.MOD, _d)
            else:
                return (_d, (c + d) % Fibonacci.MOD)

    @staticmethod
    def nth(n):
        return Fibonacci._helper(n)[0]

def main():
    for _ in range(int(input())):
        print(Fibonacci.nth(2 + int(input())))

if __name__ == "__main__":
    main()