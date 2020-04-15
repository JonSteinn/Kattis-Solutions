from collections import Counter

class TicTacToe:
    O = 'O'
    X = 'X'
    EMPTY = '.'

    def __init__(self, mat):
        self.mat = mat

    def is_valid(self):
        x,o = self.__counts()
        if o > x or abs(x-o) > 1:
            return False
        win_sequences, winners = self.__wins()
        if len(winners) == 2:
            return False
        if len(winners) == 0:
            return True
        if (TicTacToe.O in winners and x > o) or (TicTacToe.X in winners and x == o):
            return False
        if len(win_sequences) == 1:
            return True
        if len(win_sequences) == 2 and self.__are_connected(win_sequences):
            return True
        return False

    def __wins(self):
        winners = set()
        win_sequences = []
        self.__check_rows(winners, win_sequences)
        self.__check_columns(winners, win_sequences)
        self.__check_diagonals(winners, win_sequences)
        return win_sequences, winners

    def __check_rows(self, winners, win_sequences):
        for row in range(3):
            if self.mat[row][0] == self.mat[row][1] == self.mat[row][2] != TicTacToe.EMPTY:
                winners.add(self.mat[row][0])
                win_sequences.append({(row,0),(row,1),(row,2)})

    def __check_columns(self, winners, win_sequences):
        for col in range(3):
            if self.mat[0][col] == self.mat[1][col] == self.mat[2][col] != TicTacToe.EMPTY:
                winners.add(self.mat[0][col])
                win_sequences.append({(0,col),(1,col),(2,col)})

    def __check_diagonals(self, winners, win_sequences):
        if self.mat[0][0] == self.mat[1][1] == self.mat[2][2] != TicTacToe.EMPTY:
            winners.add(self.mat[0][0])
            win_sequences.append({(0,0),(1,1),(2,2)})
        if self.mat[2][0] == self.mat[1][1] == self.mat[0][2] != TicTacToe.EMPTY:
            winners.add(self.mat[2][0])
            win_sequences.append({(2,0),(1,1),(0,2)})

    def __are_connected(self, sequences):
        first,second = sequences
        return len(first.intersection(second)) == 1
        
    def __counts(self):
        return (lambda c: (c[TicTacToe.X],c[TicTacToe.O]))(Counter(sum(self.mat,[])))

def main():
    for i in range(int(input())):
        if i:
            input()
        mat = [list(input()) for _ in range(3)]
        print('yes' if TicTacToe(mat).is_valid() else 'no')

if __name__ == "__main__":
    main()