from heapq import heappop, heappush
from math import sqrt

class MaxHeap:
    @staticmethod
    def construct_init_heap_from_input():
        heap = MaxHeap()
        for v,init_cost in enumerate(map(int,input().split())):
            if init_cost != -1:
                heap.push(v, init_cost)
        return heap

    def __init__(self):
        self.h = []

    def push(self, v, cost):
        heappush(self.h, (-cost, v))
        
    def pop(self):
        cost, v = heappop(self.h)
        return -cost, v

    def __bool__(self):
        return bool(self.h)

class Graph:
    @staticmethod
    def construct_from_input():
        g = Graph(int(input()))
        for _ in range(len(g.vertices)-1):
            g.add_parent(*map(int, input().split()))
        return g

    class Edge:
        def __init__(self):
            self.parent = -1
            self.percent = 0.0
            self.super = False

    def __init__(self, v):
        self.vertices = [Graph.Edge() for _ in range(v)]

    def add_parent(self, parent, child, perc, sup):
        self.vertices[child-1].parent = parent-1
        self.vertices[child-1].percent = perc/100.0
        self.vertices[child-1].super = bool(sup)

    def root_cost(self, heap):
        best = [-1]*len(self.vertices)
        largest = 0
        while heap:
            cost, curr = heap.pop()
            if self.vertices[curr].parent == -1:
                largest = max(largest, cost)
                continue

            if self.vertices[curr].super:
                cost = sqrt(cost) / self.vertices[curr].percent
            else:
                cost = cost / self.vertices[curr].percent
            if best[self.vertices[curr].parent] <= cost:
                best[self.vertices[curr].parent] = cost
                heap.push(self.vertices[curr].parent, cost)
        return largest

def main():
    print('%.3f' % Graph.construct_from_input().root_cost(MaxHeap.construct_init_heap_from_input()))

if __name__ == "__main__":
    main()