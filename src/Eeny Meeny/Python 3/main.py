def teams(offset, players):
    teams = [[],[]]
    alter, index = (0,0)
    while players:
        index = (index + offset) % len(players)
        teams[alter].append(players.pop(index))
        alter = (alter + 1) % 2
    return tuple(teams)

def output(t1,t2):
    print(len(t1))
    print('\n'.join(t1))
    print(len(t2))
    print('\n'.join(t2))

def main():
    output(*teams(len(input().split()) - 1, [input() for _ in range(int(input()))]))

if __name__ == "__main__":
    main()