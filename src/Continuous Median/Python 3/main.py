from heapq import heappop, heappush

class MinHeap:
    def __init__(self):
        self.h = []

    def __len__(self):
        return len(self.h)

    def push(self, n):
        heappush(self.h, n)

    def head(self):
        return self.h[0]

    def pop(self):
        return heappop(self.h)

class MaxHeap:
    def __init__(self):
        self.h = []

    def __len__(self):
        return len(self.h)

    def push(self, n):
        heappush(self.h, -n)

    def head(self):
        return -self.h[0]

    def pop(self):
        return -heappop(self.h)

class MedianDataArray:
    def __init__(self):
        self.max = MaxHeap() # holds lowest len/2 elements
        self.min = MinHeap() # holds largest len/2 elements
        # If odd # of elements, let max heap carry the additional one

    def add(self, n):
        if not self.max:
            self.max.push(n)
        else:
            if n > self.max.head():
                self.min.push(n)
                if len(self.min) > len(self.max):
                    self.max.push(self.min.pop())
            else:
                self.max.push(n)
                if len(self.max) > len(self.min)+1:
                    self.min.push(self.max.pop())

    def median(self):
        # assumes at least one elem
        if len(self.max) == len(self.min):
            return (self.max.head() + self.min.head())//2
        else:
            return self.max.head()

def median_sum(data):
    m = MedianDataArray()
    s = 0
    for x in data:
        m.add(x)
        s += m.median()
    return s

def main():
    for _ in range(int(input())):
        input()
        print(median_sum(map(int,input().split())))

if __name__ == "__main__":
    main()