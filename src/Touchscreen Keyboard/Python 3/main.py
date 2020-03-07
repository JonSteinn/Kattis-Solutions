class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def manhattan_distance_to(self, another):
        return abs(self.x-another.x) + abs(self.y - another.y)

keyboard = ['qwertyuiop','asdfghjkl','zxcvbnm']
key_to_coord = {}
for y, keyboard_row in enumerate(keyboard):
    for x, key in enumerate(keyboard_row):
        key_to_coord[key] = Point(x,y)

def comparator(w1,w2):
    return sum(key_to_coord[a].manhattan_distance_to(key_to_coord[b]) for a,b in zip(w1,w2))

for _ in range(int(input())):
    typed, suggested = tuple(input().split())
    suggestions = sorted(
        ((lambda z: (z,comparator(typed, z)))(input()) for _ in range(int(suggested))),
        key=lambda x: (x[1],x[0])
    )
    for a,b in suggestions:
        print(f'{a} {b}')
