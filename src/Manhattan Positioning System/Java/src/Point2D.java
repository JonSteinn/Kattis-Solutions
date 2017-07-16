/**
 * A 2d point which can be compared with dictionary ordering.
 */
public class Point2D implements Comparable<Point2D> {

    // Coordinates
    private int x, y;

    /**
     * Point2D constructor.
     *
     * @param x Horizontal coordinate
     * @param y Vertical coordinate
     */
    public Point2D(int x, int y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Coordinate getter.
     *
     * @return the x coordinate
     */
    public int getX() {
        return this.x;
    }

    /**
     * Coordinate getter.
     *
     * @return the y coordinate
     */
    public int getY() {
        return this.y;
    }

    /**
     * Prime times variable hash, summed over all variable.
     *
     * @return bucket index
     */
    @Override
    public int hashCode() {
        return 31 * this.x + 47 * this.y;
    }

    /**
     * Coordinate wise equality. No error handling.
     *
     * @param o another point (exception if not)
     * @return true iff x1 == x2 && y1 == y2
     */
    @Override
    public boolean equals(Object o) {
        Point2D other = (Point2D)o;
        return this.x == other.x && this.y == other.y;
    }

    /**
     * For debugging.
     *
     * @return (x,y) format
     */
    @Override
    public String toString() {
        return "(" + this.x + "," + this.y + ")";
    }

    /**
     * Lexicographical order.
     *
     * @param o another point.
     * @return less than 0 if this is less than o, more than 0 if this is more than o, 0 otherwise
     */
    @Override
    public int compareTo(Point2D o) {
        int dy = Integer.compare(this.y, o.y);
        return dy == 0 ? Integer.compare(this.x, o.x) : dy;
    }
}
