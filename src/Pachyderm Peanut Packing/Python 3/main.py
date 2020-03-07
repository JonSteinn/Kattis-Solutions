class Point:
    def __init__(self, x, y, size):
        self.x = float(x)
        self.y = float(y)
        self.size = size

    def __repr__(self):
        return f'({self.x}, {self.y}) : {self.size}'

class Rectangle:
    def __init__(self, x1, y1, x2, y2, size):
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.x2 = float(x2)
        self.y2 = float(y2)
        self.size = size

    def __repr__(self):
        return f'[({self.x1}, {self.y1}) - ({self.x2}, {self.y2})] : {self.size}'

    def contains(self, point):
        return self.x1 <= point.x <= self.x2 and self.y1 <= point.y <= self.y2

def find_box(peanut, boxes):
    for box in boxes:
        if box.contains(peanut):
            return box.size if peanut.size[0] != box.size[0] else 'correct'
    return 'floor'

def test_case():
    box_cnt = int(input())
    if box_cnt == 0:
        return False
    # Can search smarter (closer rectangle first) but guessing bruteforce works fine here
    boxes = [Rectangle(*tuple(input().split())) for _ in range(box_cnt)]
    for _ in range(int(input())):
        peanut = Point(*tuple(input().split()))
        print(f'{peanut.size} {find_box(peanut, boxes)}')
    return True

def main():
    while True:
        if not test_case():
            break

if __name__ == "__main__":
    main()
