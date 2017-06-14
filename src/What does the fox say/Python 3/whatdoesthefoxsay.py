for i in range(int(input())):
    lst = input().split()
    sounds = set()
    while True:
        line = input().split()
        if len(line) == 3:
            sounds.add(line[2])
        else:
            print(" ".join(filter(lambda x: x not in sounds, lst)))
            break
