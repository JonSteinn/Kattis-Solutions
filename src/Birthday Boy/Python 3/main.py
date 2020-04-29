class Birthday:
    ACCUMULATED_DAYS_IN_MONTH = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    DAYS_IN_YEAR = 365

    @staticmethod
    def day_to_md(day):
        for i in range(11,-1,-1):
            if day >= Birthday.ACCUMULATED_DAYS_IN_MONTH[i]:
                m = str(i + 1)
                d = str(day - Birthday.ACCUMULATED_DAYS_IN_MONTH[i] + 1)
                break
        m = m if len(m) == 2 else f'0{m}'
        d = d if len(d) == 2 else f'0{d}'
        return f'{m}-{d}'

    def __init__(self):
        self.in_use = set()
        self.possible = {}

    def add(self, m, d):
        bday = Birthday.ACCUMULATED_DAYS_IN_MONTH[m-1] + d-1
        self.in_use.add(bday)
        if bday in self.possible:
            del self.possible[bday]
        prior = 364 if bday == 0 else bday - 1
        while prior in self.in_use:
            prior = 364 if prior == 0 else prior -1
        self.possible[prior] = 0


    def find_best(self):
        best = -1

        for k in self.possible.keys():
            prev = 364 if k == 0 else k-1
            while prev not in self.in_use:
                self.possible[k] += 1
                prev = 364 if prev == 0 else prev-1
            best = max(best, self.possible[k])

        lis = sorted((k for k,v in self.possible.items() if v == best))

        if lis[-1] >= 300:
            for x in lis:
                if x >= 300:
                    return Birthday.day_to_md(x)
        else:
            return Birthday.day_to_md(lis[0])

def main():
    bd = Birthday()
    n = int(input())
    for _ in range(n):
        _, date = input().split()
        bd.add(*map(int, date.split('-')))
    print(bd.find_best())

if __name__ == "__main__":
    main()
