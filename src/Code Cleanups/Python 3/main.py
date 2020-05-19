class Push:
    def __init__(self):
        self.cleans = 0
        self.dirt = []

    def increment_all(self):
        for i,x in enumerate(self.dirt):
            self.dirt[i] = x+1

    def dirt_sum(self):
        return sum(self.dirt)

    def reset(self):
        self.cleans += 1
        self.dirt = []

    def extend(self):
        self.dirt.append(0)

    def finish_year(self):
        if self.dirt:
            self.cleans +=1

    def __str__(self):
        return str(self.cleans)

def cleans(dirty_days):
    p = Push()
    for day in range(1,366):
        p.increment_all()
        if p.dirt_sum() >= 20:
            p.reset()
        if day in dirty_days:
            p.extend()
    p.finish_year()
    return p

def main():
    input() # Dump
    print(cleans(set(map(int,input().split()))))

if __name__ == "__main__":
    main()