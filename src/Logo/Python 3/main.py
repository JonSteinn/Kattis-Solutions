import math
from typing import Iterable, Tuple

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def move(self, direction: "Vector", magnitute: float) -> None:
        self.x += direction.x * magnitute
        self.y += direction.y * magnitute

    def distance_to(self, other: "Point") -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        
    def __str__(self) -> str:
        return f"({self.x},{self.y})"

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def rotate_left(self, degrees: float) -> None:
        rad = math.radians(degrees)
        x = self.x * math.cos(rad) - self.y * math.sin(rad)
        y = self.x * math.sin(rad) + self.y * math.cos(rad)
        self.x, self.y = x, y

    def __str__(self) -> str:
        return f"<{self.x},{self.y}>"

def test_case(commands: Iterable[Tuple[str, str]]):
    direction = Vector(0,1)
    position = Point(0,0)
    for cmd, val in commands:
        if cmd == "fd":
            position.move(direction, int(val))
        elif cmd == "lt":
            direction.rotate_left(int(val))
        elif cmd == "rt":
            direction.rotate_left(-int(val))
        else:
            position.move(direction, -int(val))
    print(round(position.distance_to(Point(0,0))))

for _ in range(int(input())):
    test_case((input().split() for _ in range(int(input()))))