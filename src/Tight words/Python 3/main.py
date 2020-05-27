import sys

class TightWords:
    MEMORY = [[[-1] * 100 for _ in range(10)] for _ in range(10)]
    ALPH_MIN, ALPH_MAX = 0,-1

    @staticmethod
    def _starting_with(start, remaining_length):
        if remaining_length == 0:
            return 1
        if TightWords.MEMORY[TightWords.ALPH_MAX][start][remaining_length] == -1:
            total = TightWords._starting_with(start, remaining_length-1)
            if start < TightWords.ALPH_MAX:
                total += TightWords._starting_with(start+1, remaining_length-1)
            if start > TightWords.ALPH_MIN:
                total += TightWords._starting_with(start-1, remaining_length-1)
            TightWords.MEMORY[TightWords.ALPH_MAX][start][remaining_length] = total
            return total
        return TightWords.MEMORY[TightWords.ALPH_MAX][start][remaining_length]

    @staticmethod
    def count(alphabet_max, length):
        TightWords.ALPH_MAX = alphabet_max
        return sum(TightWords._starting_with(i,length-1) for i in range(alphabet_max+1))

    @staticmethod
    def percentage(alphabet_max, length):
        return TightWords.count(alphabet_max, length)*100 / (alphabet_max+1)**length

def main():
    for line in sys.stdin:
        k,n = map(int,line.split())
        print('%.7f' % TightWords.percentage(k,n))

if __name__ == "__main__":
    main()