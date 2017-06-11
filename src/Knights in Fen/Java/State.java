import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by Jonni on 6/11/2017.
 */
public class State {

    private static int movement[] = {-2,-1,1,2};
    private static char[][] goal = {
        {'b','b','b','b','b'},
        {'w','b','b','b','b'},
        {'w','w','x','b','b'},
        {'w','w','w','w','b'},
        {'w','w','w','w','w'}
    };

    private char[][] board;

    public State(char[][] board) {
        this.board = board;
    }

    public boolean isGoalState() {
        return Arrays.deepEquals(this.board, State.goal);
    }

    public int heuristic() {
        int counter = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (this.board[i][j] != 'x' && this.board[i][j] != State.goal[i][j]) {
                    counter++;
                }
            }
        }
        return counter;
    }

    public Iterable<State> neighbors() {
        Set<State> set = new HashSet<>();
        int[] x = findX();
        for (int i : movement) {
            for (int j : movement) {
                if (Math.abs(i) + Math.abs(j) == 3) {
                    if (validIndex(x[0] + i) && validIndex(x[1] + j)) {
                        State tmp = new State(this.copyBoard());
                        char knight = tmp.board[x[0] + i][x[1] + j];
                        tmp.board[x[0] + i][x[1] + j] = 'x';
                        tmp.board[x[0]][x[1]] = knight;
                        set.add(tmp);
                    }
                }
            }
        }
        return set;
    }

    private char[][] copyBoard() {
        return new char[][]{
                {board[0][0],board[0][1],board[0][2],board[0][3],board[0][4]},
                {board[1][0],board[1][1],board[1][2],board[1][3],board[1][4]},
                {board[2][0],board[2][1],board[2][2],board[2][3],board[2][4]},
                {board[3][0],board[3][1],board[3][2],board[3][3],board[3][4]},
                {board[4][0],board[4][1],board[4][2],board[4][3],board[4][4]}
        };
    }

    private boolean validIndex(int i) {
        return i >= 0 && i < 5;
    }

    private int[] findX() {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (board[i][j] == 'x') return new int[]{i,j};
            }
        }
        return new int[]{};
    }


    @Override
    public String toString() {
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                str.append(this.board[i][j]);
            }
            str.append('\n');
        }
        return str.toString();
    }

    @Override
    public boolean equals(Object o) {
        return Arrays.deepEquals(this.board, ((State)o).board);
    }

    @Override
    public int hashCode() {
        return Arrays.deepHashCode(this.board);
    }
}
