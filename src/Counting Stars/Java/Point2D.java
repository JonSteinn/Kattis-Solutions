import java.util.HashSet;
import java.util.Set;

/**
 * Created by Jonni on 6/5/2017.
 */
public class Point2D {
    public int x, y;

    public Point2D(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Iterable<Point2D> neighbors(int m, int n, boolean[][] sky) {
        Set<Point2D> temp = new HashSet<>();
        try {
            if (y > 0 && sky[y - 1][x]) temp.add(new Point2D(x, y - 1));
            if (x > 0 && sky[y][x - 1]) temp.add(new Point2D(x - 1, y));
            if (y < m - 1 && sky[y + 1][x]) temp.add(new Point2D(x, y + 1));
            if (x < n - 1 && sky[y][x + 1]) temp.add(new Point2D(x + 1, y));
        } catch (ArrayIndexOutOfBoundsException ex) {
            ex.printStackTrace();
        }
        return temp;
    }

    @Override
    public boolean equals(Object o) {
        Point2D other = (Point2D)o;
        return this.x == other.x && this.y == other.y;
    }

    @Override
    public int hashCode() {
        return 31 * this.x + this.y;
    }
}