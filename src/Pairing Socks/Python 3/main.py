from collections import deque

def pair(n,stack):
    aux = deque()
    moves = 0
    while True:
        if aux and stack:
            if aux[0] == stack[0]:
                aux.popleft()
                stack.popleft()
            else:
                aux.appendleft(stack.popleft())
        elif aux:
            return 'impossible'
        elif stack:
            aux.appendleft(stack.popleft())
        else:
            return moves
        moves += 1

def main():
    n = int(input())
    stack = deque(map(int,input().split()))
    print(pair(n,stack))

if __name__ == "__main__":
    main()