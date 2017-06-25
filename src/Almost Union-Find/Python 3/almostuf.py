# Not really a good approach but easy to implement
# I'm guessing using uf and keeping tracks of children would be better
# And when removing from one union, we can sink it to a leaf and remove
# Will try that approach sometime...

class Sets:
    def __init__(self, n):
        self.elements = n
        self.sets = [{i} for i in range(n)]
        self.set_map = [i for i in range(n)]

    def union(self, i, j):
        if self.__shared__(i, j):
            return
        if len(self.sets[self.set_map[i]]) > len(self.sets[self.set_map[j]]):
            self.__transfer__(j, i)
        else:
            self.__transfer__(i, j)

    def move(self, i, j):
        if self.__shared__(i, j):
            return
        self.sets[self.set_map[i]].discard(i)
        self.sets[self.set_map[j]].add(i)
        self.set_map[i] = self.set_map[j]

    def count(self, i):
        return len(self.sets[self.set_map[i]])

    def set_sum(self, i):
        return sum(self.sets[self.set_map[i]])

    def command(self, k, lst):
        if k == 1:
            self.union(lst[0], lst[1])
        elif k == 2:
            self.move(lst[0], lst[1])
        else:
            size = self.count(lst[0])
            print(size, self.set_sum(lst[0]) + size)

    def __transfer__(self, f, t):
        old_set = self.set_map[f]
        new_set = self.set_map[t]
        for e in self.sets[old_set]:
            self.set_map[e] = new_set
            self.sets[new_set].add(e)
        self.sets[old_set].clear()

    def __shared__(self, i, j):
        return self.set_map[i] == self.set_map[j]

while True:
    try:
        a, b = tuple(map(int, input().split()))
        sets = Sets(a)
        for x in range(b):
            lis = list(map(int, input().split()))
            sets.command(lis[0], list(map(lambda z: z-1, lis[1:])))
    except EOFError:
        break
