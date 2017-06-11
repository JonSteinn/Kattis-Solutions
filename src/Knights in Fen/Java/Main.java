import java.io.*;

/**
 * Created by Jonni on 6/11/2017.
 */
public class Main {
    public static void main(String[] args) {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        try {
            int n = Integer.parseInt(in.readLine());
            for (int b = 0; b < n; b++) {
                char[][] board = new char[5][5];
                for (int i = 0; i < 5; i++) {
                    String s = in.readLine();
                    for (int j = 0; j < 5; j++) {
                        board[i][j] = s.charAt(j) == '0' ? 'w' : s.charAt(j) == '1' ? 'b' : 'x';
                    }
                }
                int moves = new AStar(new State(board)).shortestPath();
                if (moves < 0 || moves > 10) {
                    out.println("Unsolvable in less than 11 move(s).");
                } else {
                    out.printf("Solvable in %d move(s).\n", moves);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        out.close();
    }
}
