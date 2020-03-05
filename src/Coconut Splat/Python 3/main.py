class Coconut:
    @staticmethod
    def from_another(another):
        return Coconut(another.player, another.life)

    def __init__(self, player, life=2):
        self.player = player
        self.life = life

    def is_folded(self):
        return self.life == 2

    def is_fist(self):
        return self.life == 1

    def update(self):
        self.life -= 1

    def get_player(self):
        return self.player + 1

def coconut(s,p):
    seats = [Coconut(i) for i in range(p)]
    next = 0
    while len(seats) > 1:
        next = (next + s) % len(seats)
        if seats[next].is_folded():
            seats[next].update()
            seats.insert(next, Coconut.from_another(seats[next]))
        elif seats[next].is_fist():
            seats[next].update()
            next += 1
        else:
            seats.pop(next)
    return seats[0].get_player()

def main():
    s,p = tuple(map(int, input().split()))
    print(coconut(s-1,p))


if __name__ == "__main__":
    main()