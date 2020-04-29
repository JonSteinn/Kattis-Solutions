from math import e
def derangement(n):
    return 

class Factorial:
    MEM = [1]

    @staticmethod
    def factorial(n):
        while len(Factorial.MEM) <= n:
            Factorial.MEM.append(Factorial.MEM[-1] * len(Factorial.MEM))
        return Factorial.MEM[n]

    @staticmethod
    def prob(n):
        if n < 9:
            f = Factorial.factorial(n)
            d = round(f/e)
            return 1-d/f
        return 1-1/e

def main():
    print('%.6f' % Factorial.prob(int(input())))

if __name__ == "__main__":
    main()