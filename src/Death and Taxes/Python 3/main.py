class Stock:
    def __init__(self):
        self.shares = 0
        self.average_cost = 0
        self.profit = 0
        self.dead = False

    def buy(self, x, y):
        new_share_count = self.shares + x
        self.average_cost = (self.shares * self.average_cost + x * y) / new_share_count
        self.shares = new_share_count

    def sell(self, x, y):
        self.shares -= x

    def split(self, x):
        self.shares *= x
        self.average_cost /= x

    def merge(self, x):
        self.average_cost *= x
        self.shares //= x

    def die(self, y):
        self.dead = True
        if y > self.average_cost:
            self.profit = self.shares * (y - (y - self.average_cost) * 0.3)
        else:
            self.profit = self.shares * y

    def action(self, cmd, *args):
        if cmd == 'buy':
            self.buy(*map(int, args))
        elif cmd == 'sell':
            self.sell(*map(int, args))
        elif cmd == 'split':
            self.split(*map(int, args))
        elif cmd == 'merge':
            self.merge(*map(int, args))
        else:
            self.die(*map(int, args))

    def __str__(self):
        return '%.2f' % self.profit

def main():
    s = Stock()
    while not s.dead:
        s.action(*input().split())
    print(s)



if __name__ == "__main__":
    main()