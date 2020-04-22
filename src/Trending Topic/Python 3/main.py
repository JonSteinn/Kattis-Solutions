from collections import deque, Counter

class WordCounter:
    def __init__(self):
        self.days = deque()
        self.counter = Counter()

    def add_day(self, lines):
        if len(self.days) == 7:
            day = self.days.popleft()
            for k,v in day.items():
                self.counter[k] -= v
        day_counter = Counter()
        for line in lines:
            for word in line.split():
                if len(word) > 3:
                    day_counter[word] += 1
                    self.counter[word] += 1
        self.days.append(day_counter)

    def query(self, top):
        print(f'<top {top}>')
        counter = 0
        s_lis = sorted(self.counter.items(), key=lambda z: (-z[1],z[0]))
        for i, (w, c) in enumerate(s_lis):
            if counter >= top and c != s_lis[i-1][1]:
                break
            print(w,c)
            counter += 1
        print(f'</top>')

def process_day():
    lines = []
    while True:
        lines.append(input())
        if lines[-1].startswith('</'):
            lines.pop()
            break
    return lines

def main():
    try:
        wc = WordCounter()
        while True:
            cmd = input()
            if cmd.startswith('<te'):
                wc.add_day(process_day())
            elif cmd.startswith('<t'):
                wc.query(int(cmd.split()[1]))
    except EOFError:
        pass

if __name__ == "__main__":
    main()