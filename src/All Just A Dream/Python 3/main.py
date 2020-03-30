from itertools import islice

class Plot:
    def __init__(self):
        self.events = {}
        self.next_index = 0

    def add_event(self, evt):
        self.events[evt] = self.next_index
        self.next_index += 1

    def dreamify(self, amount):
        for _ in range(amount):
            self.events.popitem() # LIFO for py-dicts
            self.next_index -= 1

    def check_scenario(self, scenarios):
        to_rem, must_remain = 0,-1
        for s in scenarios:
            if s[0] == '!':
                ev = s[1:]
                if ev in self.events:
                    to_rem = max(to_rem, len(self.events)-self.events[ev])
            else:
                if s not in self.events:
                    return 'Plot Error'
                else:
                    must_remain = max(self.events[s], must_remain)
        if to_rem == 0:
            return 'Yes'
        if must_remain >= len(self.events)-to_rem:
            return 'Plot Error'
        return f'{to_rem} Just A Dream'
    
def main():
    plot = Plot()
    for _ in range(int(input())):
        line = input().split()
        if line[0] == 'E':
            plot.add_event(line[1])
        elif line[0] == 'D':
            plot.dreamify(int(line[1]))
        else:
            print(plot.check_scenario(islice(line,2,None)))

if __name__ == "__main__":
    main()