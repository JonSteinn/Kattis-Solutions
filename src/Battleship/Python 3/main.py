def result(ships):
    if all(ships) or not any(ships):
        return 'draw'
    if ships[0]:
        return 'player one wins'
    return 'player two wins'

def simulate(ships, cmds):
    dump,turn = False,False
    for x,y in cmds:
        if dump:
            continue
        if (x,y) in ships[not turn]: # Hit
            ships[not turn].remove((x,y))
            if not ships[not turn]: # if other has none left
                if turn: # If p2 turn, game is over
                    dump = True
                else: # If p1 turn, p2 has one chance
                    turn = not turn
        elif turn and not ships[turn]: # not a hit and it was p2 turn and hi has none left
            dump = True
        else: # Normal non-hit moves
            turn = not turn
    return result(ships)

def test_case(w,h,n):
    ships = (set(),set())
    for player in range(2):
        for _y in range(h):
            for x,c in enumerate(input().rstrip()):
                if c == '#':
                    ships[player].add((x,h-1-_y))
    cmds = (map(int,input().split()) for _ in range(n))
    print(simulate(ships,cmds))

def main():
    for _ in range(int(input())):
        w,h,n = map(int,input().split())
        test_case(w,h,n)

if __name__ == "__main__":
    main()