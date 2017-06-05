import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

/**
 * Created by Jonni on 6/5/2017.
 */
public class Sky {
    private int m, n;
    private boolean[][] sky;
    private ArrayList<Set<Point2D>> stars;
    private Set<Point2D> visited;

    public Sky(Kattio io) {
        this.m = io.getInt();
        this.n = io.getInt();
        this.sky = new boolean[m][n];
        this.stars = new ArrayList<>();
        this.visited = new HashSet<>();
        for (int i = 0; i < m; i++) {
            String row = io.getWord();
            for (int j = 0; j < n; j++) {
                this.sky[i][j] = row.charAt(j) == '-';
            }
        }
        count();
    }

    private void count() {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (this.sky[i][j]) {
                    Point2D point = new Point2D(j,i);
                    if (!visited.contains(point)) {
                        fill(point);
                    }
                }
            }
        }
    }

    private void fill(Point2D point) {
        Set<Point2D> next = new HashSet<>();
        Stack<Point2D> waiting = new Stack<>();
        waiting.add(point);
        while (!waiting.isEmpty()) {
            Point2D curr = waiting.pop();
            if (visited.add(curr)) {
                next.add(curr);
                for (Point2D neighbor : curr.neighbors(m,n,sky)) {
                    if (!visited.contains(neighbor)) {
                        waiting.push(neighbor);
                    }
                }
            }
        }
        stars.add(next);
    }

    public int numberOfStars() {
        return this.stars.size();
    }
}
