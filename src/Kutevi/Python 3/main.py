from collections import deque
from itertools import combinations as C

def find_all_possible(known):
    possible = [False]*360
    for x in known:
        possible[x] = True

    stack = deque()
    for a1 in known.copy():
        a2 = a1
        for a in [(360+a1-a2)%360, (360+a2-a1)%360, (a1+a2) % 360]:
            if not possible[a]:
                stack.append(a)
                known.add(a)
                possible[a] = True
    for a1,a2 in C(known,2):
        for a in [(360+a1-a2)%360, (360+a2-a1)%360, (a1+a2) % 360]:
            if not possible[a]:
                stack.append(a)
                known.add(a)
                possible[a] = True
    
    while stack:
        a1 = stack.pop()
        a2 = a1
        for a in [(360+a1-a2)%360, (360+a2-a1)%360, (a1+a2) % 360]:
            if not possible[a]:
                stack.append(a)
                known.add(a)
                possible[a] = True
        for a2 in known.copy():
            for a in [(360+a1-a2)%360, (360+a2-a1)%360, (a1+a2) % 360]:
                if not possible[a]:
                    stack.append(a)
                    known.add(a)
                    possible[a] = True
    return possible


def main():
    input()#DUMP
    possible = find_all_possible(set(map(int,input().split())))
    for x in map(int,input().split()):
        print('YES' if possible[x] else 'NO')

if __name__ == "__main__":
    main()