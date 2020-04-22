from heapq import heappop, heappush

class SupplyAndDemand:
    def __init__(self, shares, value):
        self.shares = shares
        self.value = value
    def __str__(self):
        return f'{self.shares} at {self.value}'
    def __repr__(self):
        return str(self)

class Supply(SupplyAndDemand):
    def __lt__(self, other):
        return self.value < other.value
    def __le__(self, other):
        return self.value <= other.value

class Demand(SupplyAndDemand):
    def __lt__(self, other):
        return self.value > other.value
    def __le__(self, other):
        return self.value >= other.value
    
class Stock:
    def __init__(self):
        self.supply = []
        self.demand = []
        self.last_trade = -1

    def buy(self, shares, value):
        heappush(self.demand, Demand(shares, value))
        self._simulate_trades()

    def sell(self, shares, value):
        heappush(self.supply, Supply(shares, value))
        self._simulate_trades()

    def _simulate_trades(self):
        while self.supply and self.demand and self.supply[0] <= self.demand[0]:
            self.last_trade = self.supply[0].value

            if self.supply[0].shares == self.demand[0].shares:
                heappop(self.supply)
                heappop(self.demand)
            elif self.supply[0].shares < self.demand[0].shares:
                self.demand[0].shares -= heappop(self.supply).shares
            else:
                self.supply[0].shares -= heappop(self.demand).shares

    def __str__(self):
        ask = self.supply[0].value if self.supply else '-'
        bid = self.demand[0].value if self.demand else '-'
        price = self.last_trade if self.last_trade != -1 else '-'
        return f'{ask} {bid} {price}'
    
    def __repr__(self):
        return str(self)
    
def main():
    for _ in range(int(input())):
        stock = Stock()
        for _ in range(int(input())):
            cmd, shares, _, _, value = input().split()
            if cmd[0] == 'b':
                stock.buy(int(shares), int(value))
            else:
                stock.sell(int(shares), int(value))
            print(stock)


if __name__ == "__main__":
    main()