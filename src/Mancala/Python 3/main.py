import heapq

def print_board(board):
    for i in range(1,len(board),10):
        print(' '.join(map(str,board[i:i+10])))

def find_board(n):
    board = [n] # includes Ruma
    zeros = []
    while board[0] > 0:
        if not zeros:
            for i in range(len(board) - 1, -1, -1):
                board[i] -= 1
                 # The Ruma shouldn't be placed here but since
                 # it would break the loop, it doesn't matter
                if board[i] == 0:
                    heapq.heappush(zeros, i)
            board.append(len(board))
        else:
            next_empty = heapq.heappop(zeros)
            board[next_empty] = next_empty
            for i in range(next_empty - 1, -1, -1):
                board[i] -= 1
                if board[i] == 0:
                    heapq.heappush(zeros, i)

    return board

def case(c, n):
    board = find_board(n)
    print(f'{c} {len(board)-1}')
    print_board(board)

def main():
    n = int(input())
    for _ in range(n):
        c, n = tuple(map(int, input().split()))
        case(c,n)

if __name__ == "__main__":
    main()
