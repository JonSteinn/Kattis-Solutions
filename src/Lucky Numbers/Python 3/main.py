from itertools import islice

class LuckyNumbers:
    ALL = '0123456789'

    @staticmethod
    def number_of_lucky_numbers(n):
        return LuckyNumbers.__count_all(['0'] * n, 0, n)

    @staticmethod
    def __count_all(number, i, n):
        s = 0
        if i == 0:
            for c in islice(LuckyNumbers.ALL,1,None):
                number[i] = c
                s += LuckyNumbers.__count_all(number, i + 1, n)
        elif i == n - 1:
            for c in LuckyNumbers.ALL:
                number[i] = c
                if int(''.join(number)) % n == 0:
                    s += 1
        else:
            for c in LuckyNumbers.ALL:
                number[i] = c
                if int(''.join(islice(number, 0, i+1))) % (i+1) == 0:
                    s += LuckyNumbers.__count_all(number, i + 1, n)
        return s

def main():
    n = int(input())
    print(LuckyNumbers.number_of_lucky_numbers(n))

if __name__ == "__main__":
    main()