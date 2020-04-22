#############################################
# Some absolutely shameful c/p work here... #
#############################################

from collections import deque

class Foosball:
    def __init__(self, wo, bo, wd, bd, *rest):
        self.potential_legacies = {(wo,wd): 0, (bo,bd): 0}
        self.white = [wo,wd]
        self.black = [bo,bd]
        self.queue = deque([name for name in rest])
        self.dynasties = []
        self.best = -1

    def done(self):
        if (self.black[0],self.black[1]) in self.potential_legacies:
            v = self.potential_legacies[(self.black[0],self.black[1])]
            if v == self.best:
                self.dynasties.append((self.black[0],self.black[1]))
            elif v > self.best:
                self.best = v
                self.dynasties = [(self.black[0],self.black[1])]
            del self.potential_legacies[(self.black[0],self.black[1])]
        elif (self.black[1],self.black[0]) in self.potential_legacies:
            v = self.potential_legacies[(self.black[1],self.black[0])]
            if v == self.best:
                self.dynasties.append((self.black[1],self.black[0]))
            elif v > self.best:
                self.best = v
                self.dynasties = [(self.black[1],self.black[0])]
            del self.potential_legacies[(self.black[1],self.black[0])]
        if (self.white[0],self.white[1]) in self.potential_legacies:
            v = self.potential_legacies[(self.white[0],self.white[1])]
            if v == self.best:
                self.dynasties.append((self.white[0],self.white[1]))
            elif v > self.best:
                self.best = v
                self.dynasties = [(self.white[0],self.white[1])]
            del self.potential_legacies[(self.white[0],self.white[1])]
        elif (self.white[1],self.white[0]) in self.potential_legacies:
            v = self.potential_legacies[(self.white[1],self.white[0])]
            if v == self.best:
                self.dynasties.append((self.white[1],self.white[0]))
            elif v > self.best:
                self.best = v
                self.dynasties = [(self.white[1],self.white[0])]
            del self.potential_legacies[(self.white[1],self.white[0])]

    def white_scores(self):
        # Update legacy for white
        if (self.white[0],self.white[1]) in self.potential_legacies:
            self.potential_legacies[(self.white[0],self.white[1])] += 1
        elif (self.white[1],self.white[0]) in self.potential_legacies:
            self.potential_legacies[(self.white[1],self.white[0])] += 1

        # Check if black is best legacy
        if (self.black[0],self.black[1]) in self.potential_legacies:
            v = self.potential_legacies[(self.black[0],self.black[1])]
            if v == self.best:
                self.dynasties.append((self.black[0],self.black[1]))
            elif v > self.best:
                self.best = v
                self.dynasties = [(self.black[0],self.black[1])]
            del self.potential_legacies[(self.black[0],self.black[1])]
        elif (self.black[1],self.black[0]) in self.potential_legacies:
            v = self.potential_legacies[(self.black[1],self.black[0])]
            if v == self.best:
                self.dynasties.append((self.black[1],self.black[0]))
            elif v > self.best:
                self.best = v
                self.dynasties = [(self.black[1],self.black[0])]
            del self.potential_legacies[(self.black[1],self.black[0])]

        # Update white
        tmp = self.white[0]
        self.white[0] = self.white[1]
        self.white[1] = tmp

        # Update black
        self.queue.append(self.black.pop())
        self.black.append(self.queue.popleft())
        tmp = self.black[0]
        self.black[0] = self.black[1]
        self.black[1] = tmp

        # Set new blakc up for potential legacy
        self.potential_legacies[(self.black[1],self.black[0])] = 0

    def black_scores(self):
        # Update legacy for black
        if (self.black[0],self.black[1]) in self.potential_legacies:
            self.potential_legacies[(self.black[0],self.black[1])] += 1
        elif (self.black[1],self.black[0]) in self.potential_legacies:
            self.potential_legacies[(self.black[1],self.black[0])] += 1

        # Check if white is best legacy
        if (self.white[0],self.white[1]) in self.potential_legacies:
            v = self.potential_legacies[(self.white[0],self.white[1])]
            if v == self.best:
                self.dynasties.append((self.white[0],self.white[1]))
            elif v > self.best:
                self.best = v
                self.dynasties = [(self.white[0],self.white[1])]
            del self.potential_legacies[(self.white[0],self.white[1])]
        elif (self.white[1],self.white[0]) in self.potential_legacies:
            v = self.potential_legacies[(self.white[1],self.white[0])]
            if v == self.best:
                self.dynasties.append((self.white[1],self.white[0]))
            elif v > self.best:
                self.best = v
                self.dynasties = [(self.white[1],self.white[0])]
            del self.potential_legacies[(self.white[1],self.white[0])]

        # Update black
        tmp = self.black[0]
        self.black[0] = self.black[1]
        self.black[1] = tmp

        # Update white
        self.queue.append(self.white.pop())
        self.white.append(self.queue.popleft())
        tmp = self.white[0]
        self.white[0] = self.white[1]
        self.white[1] = tmp

        # Set new white up for potential legacy
        self.potential_legacies[(self.white[1],self.white[0])] = 0

    def get_dynasties(self):
        return self.dynasties

def main():
    input() # Dump
    fb = Foosball(*input().split())
    for r in input():
        if r == 'W':
            fb.white_scores()
        else:
            fb.black_scores()
    fb.done()
    for dynasty in fb.get_dynasties():
        print(*dynasty)

if __name__ == "__main__":
    main()