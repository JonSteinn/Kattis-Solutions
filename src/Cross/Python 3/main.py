from collections import namedtuple

class Sudoko:
    Number = namedtuple('Number', 'rows_left rows_in_use columns_left columns_in_use boxes_left boxes_in_use')
    
    def __init__(self):
        self.positions = [Sudoko.Number(set(range(9)),set(),set(range(9)),set(),set(range(9)),set()) for i in range(9)]
        self.mat = [[0 for _ in range(9)] for _ in range(9)]
        self.unknowns = 81
        self.invalid = False

    def cross_hatching(self):
        if self.invalid or self.unknowns == 0:
            return
        while self.__cross_hatching_round():
            pass

    def read_from_input(self):
        for r in range(9):
            for c,x in enumerate(input()):
                if x != '.':
                    self.__set_value(r,c,int(x))
                    if self.invalid:
                        self.__dump_input(r)
                        return

    def __invalid(self, r, c, b, x):
        return any((
            self.mat[r][c] != 0,
            r in self.positions[x-1].rows_in_use,
            c in self.positions[x-1].columns_in_use,
            b in self.positions[x-1].boxes_in_use
        ))

    def __update_numbers(self,r,c,b,x):        
        self.positions[x-1].rows_left.discard(r)
        self.positions[x-1].rows_in_use.add(r)
        self.positions[x-1].columns_left.discard(c)
        self.positions[x-1].columns_in_use.add(c)
        self.positions[x-1].boxes_left.discard(b)
        self.positions[x-1].boxes_in_use.add(b)

    def __set_value(self, r, c, x):
        b = r // 3 * 3 + c // 3
        if self.__invalid(r,c,b,x):
            self.invalid = True
            return
        self.mat[r][c] = x
        self.unknowns -= 1
        self.__update_numbers(r,c,b,x)

    def __dump_input(self,n):
        for _ in range(n+1,9):
            input()

    def __cross_hatching_round(self):
        found_some = False
        for i in range(9):
            if self.__cross_hatch_single(i):
                found_some = True
            if self.invalid or self.unknowns == 0:
                found_some = False
                break
        return found_some

    def __cross_hatch_single(self, x):
        for b in self.positions[x].boxes_left:
            free = []
            for r in (lambda z: range(z,z+3))((b//3) * 3):
                if r in self.positions[x].rows_in_use:
                    continue
                for c in (lambda z: range(z,z+3))((b%3) * 3):
                    if c in self.positions[x].columns_in_use:
                        continue
                    if self.mat[r][c] == 0:
                        free.append((r,c,b))
            if len(free) == 0:
                self.invalid = True
                return False
            if len(free) == 1:
                self.mat[free[0][0]][free[0][1]] = x+1
                self.__update_numbers(free[0][0], free[0][1], free[0][2], x+1)
                return True
        return False

    def __str__(self):
        if self.invalid:
            return 'ERROR'
        return '\n'.join(''.join('.' if x == 0 else str(x) for x in r) for r in self.mat)


def main():
    sudoko = Sudoko()
    sudoko.read_from_input()
    sudoko.cross_hatching()
    print(sudoko)

if __name__ == "__main__":
    main()