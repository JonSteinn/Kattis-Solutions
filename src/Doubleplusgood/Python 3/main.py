from itertools import combinations
from functools import reduce

class Number:
    def __init__(self,x):
        self.x = x

    def __add__(self,other):
        return Number(self.x + other.x)

    def __radd__(self, other):
        return self.x + other

    def __mul__(self,other):
        return Number(int(f'{self.x}{other.x}'))

    def __repr__(self):
        return f'{self.x}'

    def __str__(self):
        return f'{self.x}'

class Numbers:
    def __init__(self, numbers):
        self.ops = len(numbers)-1
        self.op_indices = [i for i in range(self.ops)]
        self.numbers = numbers
        self.values = {sum(numbers)}
        self.__eval_all()
        
    def get_unique_values(self):
        return len(self.values)

    def __eval_all(self):
        for i in range(1,self.ops + 1):
            for comb in combinations(self.op_indices, i):
                intervals = self.__combination_to_intervals(comb, i)
                self.values.add(self.__eval_for_intervals(intervals))

    def __eval_for_intervals(self, intervals):
        a,b = intervals.pop(0)
        s,i = 0,0
        while True:
            if i == a:
                s += reduce(lambda c,n: c*n, self.numbers[a+1:b+1], self.numbers[a])
                if not intervals:
                    s += sum(self.numbers[b+1:])
                    break
                else:
                    i = b+1
                    a,b = intervals.pop(0)
            else:
                s += self.numbers[i]
                i += 1
        return s

    def __combination_to_intervals(self, c,n):
        if n == 1:
            return [(c[0],c[0]+1)]
        lis = []
        i,j = 0,1
        while True:
            if j == n-1:
                if c[j] == c[j-1]+1:
                    lis.append((c[i],c[j]+1))
                else:
                    lis.append((c[i],c[j-1]+1))
                    lis.append((c[j],c[j]+1))
                break
            elif c[j] == c[j-1] + 1:
                j += 1
            else:
                lis.append((c[i],c[j-1]+1))
                i = j
                j = i+1
        
        return lis

def main():
    numbers = Numbers(list(map(lambda z: Number(int(z)), input().split('+'))))
    print(numbers.get_unique_values())

if __name__ == "__main__":
    main()