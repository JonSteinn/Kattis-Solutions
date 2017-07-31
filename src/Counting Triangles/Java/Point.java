/**
 * Created by Jonni on 7/31/2017.
 */
public class Point {
    public final double x, y;
    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
    @Override
    public String toString() {
        return "(" + x + "," + y + ")";
    }
    @Override
    public boolean equals(Object o) {
        Point other = (Point)o;
        return this.x == other.x && this.y == other.y;
    }
    @Override
    public int hashCode() {
        return Double.hashCode(x) ^ Double.hashCode(y);
    }
}