from collections import deque, Counter

class StopRecursion(Exception):
    pass

class Queue:
    def __init__(self, t):
        self.total = t
        self.used = 0
        self.queue = deque()

    def push(self,index,time):
        if time + self.used > self.total:
            return False
        self.queue.append((index,self.used))
        self.used += time
        return True

    def undo_push(self,time):
        self.queue.pop()
        self.used -= time

    def pop(self):
        return self.queue.popleft()

    def empty(self):
        return not self.queue

class Queues:
    def __init__(self, t):
        self.first = Queue(t)
        self.second = Queue(t)

    def __iter__(self):
        yield self.first
        yield self.second

    def used(self):
        return self.first.used, self.second.used

    def __str__(self):
        return ' '.join(f'{x}' for _,x in sorted(self.first.queue + self.second.queue, key=lambda z: z[0]))

def recursive_search(rest,queues,counter,mem):
    if not rest:
        print(queues)
        raise StopRecursion()

    stamp = (*queues.used(),counter[rest[-1][1]])
    if stamp in mem:
        return
    
    index, time = rest.pop()
    for queue in queues:
        if queue.push(index,time):
            counter[time] -= 1
            recursive_search(rest,queues,counter,mem)
            queue.undo_push(time)
            counter[time] += 1
    rest.append((index,time))

    mem.add(stamp)

def schedule_rest(t,rest,counter):
    try:
        queues = Queues(t)
        memory = set()
        recursive_search(rest,queues,counter,memory)
    except StopRecursion:
        pass

def main():
    t,_ = map(int,input().split())
    rest = sorted(enumerate(map(int,input().split())),key=lambda z: z[1])
    counter = Counter(x for _,x in rest)
    schedule_rest(t,rest,counter)

if __name__ == "__main__":
    main()