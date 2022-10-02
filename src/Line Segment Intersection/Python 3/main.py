from typing import Optional, Tuple, overload, Union

_DELTA = 1E-6

def feq(a: float, b: float) -> bool:
    return abs(a - b) < _DELTA

class Vector:
    @classmethod
    def from_points(cls, x1: float, y1: float, x2: float, y2: float) -> "Vector":
        return cls(x2 - x1, y2 - y1)

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Vector):
            return self.x == __o.x and self.y == __o.y
        raise NotImplementedError()

    def feq(self, other: "Vector") -> bool:
        return feq(self.x, other.x) and feq(self.y, other.y)

    def col_matrix_det(self, other: "Vector") -> float:
        """Determinant of:
        | self.x  other.x |
        | self.y  other.y |
        """
        return self.x * other.y - self.y * other.x

    def length_squared(self) -> float:
        return self.x ** 2 + self.y ** 2

    def is_zero_vector(self) -> bool:
        return self.x == 0 and self.y == 0
    
    def as_tuple(self) -> Tuple[float, float]:
        return (self.x, self.y)

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y)

    def __add__(self, other: object) -> "Vector":
        if not isinstance(other, Vector):
            raise NotImplementedError()
        return Vector(self.x + other.x, self.y + other.y)
    
    def __radd__(self, other: object) -> "Vector":
        return self + other

    def __sub__(self, other: object) -> "Vector":
        if not isinstance(other, Vector):
            raise NotImplementedError()
        return Vector(self.x - other.x, self.y - other.y)

    def __rsub__(self, other: object) -> "Vector":
        if not isinstance(other, Vector):
            raise NotImplementedError()
        return Vector(other.x - self.x, other.y - self.y)

    @overload
    def __mul__(self, other: float) -> "Vector":
        ...

    @overload
    def __mul__(self, other: "Vector") -> "float":
        ...

    def __mul__(self, other: object) -> Union[float, "Vector"]:
        if isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise NotImplementedError()

    @overload
    def __rmul__(self, other: float) -> "Vector":
        ...

    @overload
    def __rmul__(self, other: "Vector") -> "float":
        ...

    def __rmul__(self, other: object) -> Union[float, "Vector"]:
        return self * other
    

    def __truediv__(self, other: object) -> "Vector":
        if isinstance(other, float):
            return Vector(self.x / other, self.y / other)
        raise NotImplementedError()


Point = Vector


class LineSegment:
    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        if (x2, y2) < (x1, y1):
            x1, y1, x2, y2 = x2, y2, x1, y1
        self.pos = Point(x1, y1)
        self.vec = Vector.from_points(x1, y1, x2, y2)

    def is_point(self) -> bool:
        return self.vec.is_zero_vector()

    def collides_with_point(self, x, y) -> bool:
        if self.vec.x == 0:
            return self.pos.x == x and 0 <= y - self.pos.y <= self.vec.y
        if self.vec.y == 0:
            return self.pos.y == y and 0 <= x - self.pos.x <= self.vec.x
        return feq((y - self.pos.y) * self.vec.x, (x - self.pos.x) * self.vec.y) and 0 <= y - self.pos.y <= self.vec.y

    def intersection(self, other: "LineSegment") -> Optional[Tuple[float, ...]]:
        self_is_point, other_is_point = self.is_point(), other.is_point()            
        if self_is_point or other_is_point:
            return self._point(other, self_is_point, other_is_point)
        det = self.vec.col_matrix_det(other.vec)
        if det == 0:
            return self._zero_det(other)
        self_to_other = other.pos - self.pos
        r = self_to_other.col_matrix_det(other.vec) / det
        s = self_to_other.col_matrix_det(self.vec) / det
        if 0 <= r <= 1 and 0 <= s <= 1:
            return (self.pos + (r * self.vec)).as_tuple()
        return None

    def _collinear(self, other: "LineSegment", self_to_other: "Vector") -> Optional[Tuple[float, ...]]:
        sq = self.vec.length_squared()
        t0 = (self_to_other * self.vec)/sq
        t1 = t0 + (other.vec * self.vec)/sq
        if t1 < t0:
            t0, t1 = t1, t0
        if t1 < 0 or t0 > 1:
            return None
        # If all are collinear, just sort them and pick middle 2
        (x1, y1), (x2, y2) = sorted(
            map(
                Vector.as_tuple, 
                (self.pos, other.pos, self.pos + self.vec, other.pos + other.vec)
            )
        )[1:-1]
        if feq(x1, x2) and feq(y1, y2):
            return x1, y1
        return x1, y1, x2, y2

    def _zero_det(self, other: "LineSegment") -> Optional[Tuple[float, ...]]:
        self_to_other = other.pos - self.pos
        if self_to_other.col_matrix_det(self.vec) == 0:
            return self._collinear(other, self_to_other)
        return None

    def _point(self, other: "LineSegment", self_is_point: bool, other_is_point: bool) -> Optional[Tuple[float, ...]]:
        if self.pos == other.pos:
            return self.pos.as_tuple()
        if self_is_point and other_is_point:
            return None
        if self_is_point:
            if other.collides_with_point(self.pos.x, self.pos.y):
                return self.pos.as_tuple()
            return None
        if self.collides_with_point(other.pos.x, other.pos.y):
            return other.pos.as_tuple()
        return None


def main():
    for _ in range(int(input())):
        x1,y1,x2,y2,x3,y3,x4,y4 = map(int, input().split())
        intersection = LineSegment(x1,y1,x2,y2).intersection(LineSegment(x3,y3,x4,y4))
        if intersection is None:
            print("none")
        else:
            print(" ".join(f'{x:.2f}' for x in intersection))

if __name__ == "__main__":
    main()
