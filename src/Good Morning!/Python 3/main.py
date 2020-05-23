class Timers:
    def __init__(self):
        self.transitions = {
            1: {2,4},
            2: {3,5},
            3: {6},
            4: {5,7},
            5: {6,8},
            6: {9},
            7: {8},
            8: {9,0},
            9: set(),
            0: set()
        }
        self.all = self._generate_all()

    def _generate_all(self):
        l,s = [],set()
        self._gen_all_helper(1,l,s)
        s.add(111) # Only valid 3 repeats added manually
        return sorted(s)

    def _gen_all_helper(self, curr, lis, s):
        # One of curr
        lis.append(curr)
        as_number = int(''.join(str(x) for x in lis))
        if as_number <= 200:
            for n in self.transitions[curr]:
                self._gen_all_helper(n,lis,s)
            s.add(as_number)
        lis.pop()

        # Two of curr
        if as_number <= 200:
            lis.append(curr)
            lis.append(curr)
            as_number = int(''.join(str(x) for x in lis))
            if as_number <= 200:
                for n in self.transitions[curr]:
                    self._gen_all_helper(n,lis,s)
                s.add(as_number)
            lis.pop()
            lis.pop()

        # Skip curr
        for n in self.transitions[curr]:
            self._gen_all_helper(n,lis,s)

    def find_best(self,x):
        l,r = 0, len(self.all)-1
        while l <= r:
            m = l + (r-l)//2
            if self.all[m] == x:
                return x
            if self.all[m] < x:
                l = m+1
            else:
                r = m-1
        
        possible = []
        if r >= 0:
            possible.append(self.all[r])
        if l < len(self.all):
            possible.append(self.all[l])
        possible.sort(key=lambda z: abs(x-z))
        return possible[0]

def main():
    timers = Timers()
    for _ in range(int(input())):
        print(timers.find_best(int(input())))

if __name__ == "__main__":
    main()