class Table:
    def __init__(self):
        self.stacks = [0,0]

    def command(self,drop, amount):
        actions = []
        if drop:
            self.__from_waiter(actions,amount)
        else:
            self.__to_dish_washer(actions,amount)
        return '\n'.join(actions)

    def __from_waiter(self,a,d):
        self.stacks[1] += d
        a.append(f'DROP 2 {d}')

    def __to_dish_washer(self,a,d):
        from_one = min(d,self.stacks[0])
        if from_one != 0:
            d -= from_one
            self.stacks[0] -= from_one
            a.append(f'TAKE 1 {from_one}')
        if d != 0:
            a.append(f'MOVE 2->1 {self.stacks[1]}')
            self.stacks[0] = self.stacks[1] - d
            self.stacks[1] = 0
            a.append(f'TAKE 1 {d}')

def test_case(n):
    table = Table()
    for _ in range(n):
        print(table.command(*(lambda a,b: (a[0] == 'D', int(b)))(*input().split())))

def main():
    first = True
    while True:
        n = int(input())
        if n == 0:
            break
        if first:
            first = False
        else:
            print()
        test_case(n)

if __name__ == "__main__":
    main()