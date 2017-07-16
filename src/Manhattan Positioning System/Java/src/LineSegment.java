/**
 * An abstraction for a set of integer points in a line
 * segment so we do not need to store each point.
 */
public class LineSegment {

    // Variables
    private Point2D origin;
    private Point2D end;

    /**
     * LineSegment Constructor. Order of points does not matter
     * as the constructor will always sort them so origin is
     * lexicographically less than end.
     *
     * @param x0 x coordinate of point 0
     * @param y0 y coordinate of point 0
     * @param x1 x coordinate of point 1
     * @param y1 y coordinate of point 1
     */
    public LineSegment(int x0, int y0, int x1, int y1) {
        Point2D p0 = new Point2D(x0, y0);
        Point2D p1 = new Point2D(x1, y1);
        if (p0.compareTo(p1) < 0) {
            this.origin = p0;
            this.end = p1;
        } else {
            this.origin = p1;
            this.end = p0;
        }
    }

    /**
     * Getter for origin.
     *
     * @return a 2d point
     */
    public Point2D getOrigin() {
        return this.origin;
    }

    /**
     * Getter for end.
     *
     * @return a 2d point
     */
    public Point2D getEnd() {
        return this.end;
    }

    /**
     * We say that the line segment is a point if it's a singleton set.
     *
     * @return true iff origin == end
     */
    public boolean isPoint() {
        return this.origin.equals(this.end);
    }

    /**
     * Check if slope of segment is positive. Note that for all diamonds, the
     * slope is either -1 or 1 so we do not care for the special cases of infinities.
     *
     * @return true iff slope of segment is 1
     */
    public boolean positiveSlope() {
        return sign(this.end.getY() - this.origin.getY()) == sign(this.end.getX() - this.origin.getX());
    }

    /**
     * Given that pnt lies on the same line as the segment,
     * checks if it is contained in the segment.
     *
     * @param pnt a 2d point
     * @return true iff segment contains point
     */
    public boolean contains(Point2D pnt) {
        return this.origin.compareTo(pnt) <= 0 && this.end.compareTo(pnt) >= 0;
    }

    /**
     * Check for collision between two line segments with the same slope.
     *
     * @param other another line segment
     * @return The intersection of this and other, null if none
     */
    public LineSegment sameSlopeCollision(LineSegment other) {
        return sameLine(other) ? sameLineCollision(other) : null;
    }

    /**
     * Check for collision between two line segments with opposite slopes.
     *
     * @param other another line segment
     * @return A singleton line segment if they collide, null otherwise
     */
    public LineSegment orthogonalSlopeCollision(LineSegment other) {
        Point2D pnt = collisionPoint(other);
        if (pnt == null) return null;
        LineSegment ls = new LineSegment(pnt.getX(),pnt.getY(),pnt.getX(),pnt.getY());
        return this.contains(ls.getOrigin()) && other.contains(ls.getOrigin()) ? ls : null;
    }

    /**
     * Check if two line segments belong to the same line.
     *
     * @param other another line segment
     * @return true iff this and other lie on the same line
     */
    public boolean sameLine(LineSegment other) {
        return this.positiveSlope()
                ? this.origin.getY() - this.origin.getX() == other.origin.getY() - other.origin.getX()
                : this.origin.getX() + this.origin.getY() == other.origin.getX() + other.origin.getY();
    }

    /**
     * Prime times variable hash, summed over all variable.
     *
     * @return bucket index
     */
    @Override
    public int hashCode() {
        return 31 * this.origin.hashCode() + this.origin.hashCode();
    }

    /**
     * Equality between two line segments is based on comparing
     * origins and end points. Since they are sorted lexicographically
     * within each segment, the order does not matter. No error handling.
     *
     * @param o another segment
     * @return true iff origin and end are equal in both
     */
    @Override
    public boolean equals(Object o) {
        LineSegment other = (LineSegment)o;
        return this.origin.equals(other.origin) && this.end.equals(other.end);
    }

    /**
     * String format for segments.
     *
     * @return "(origin_x, origin_y) -> (end_x, end_y)"
     */
    @Override
    public String toString() {
        return this.origin.toString() + " -> " + this.end.toString();
    }

    /////////////////////
    // Private helpers //
    /////////////////////

    /**
     * Given that two line segments share a line, this method
     * returns their intersection. Null is returned if they
     * do not intersect.
     *
     * @param other another line segment
     * @return the intersection of two sets (line segments) of integer point
     */
    private LineSegment sameLineCollision(LineSegment other) {
        if (this.end.compareTo(other.origin) < 0 || other.end.compareTo(this.origin) < 0) {
            return null;
        } else if (this.contains(other.origin) && this.contains(other.end)) {
            return new LineSegment(other.origin.getX(), other.origin.getY(), other.end.getX(), other.end.getY());
        } else if (other.contains(this.origin) && other.contains(this.end)) {
            return new LineSegment(this.origin.getX(), this.origin.getY(), this.end.getX(), this.end.getY());
        } else if (this.contains(other.end)) {
            return new LineSegment(this.origin.getX(), this.origin.getY(), other.end.getX(), other.end.getY());
        } else {
            return new LineSegment(other.origin.getX(), other.origin.getY(), this.end.getX(), this.end.getY());
        }
    }

    /**
     * Returns the sign of a given number. 0 is counted as positive.
     *
     * @param x any integer
     * @return -1 iff x is negative, 1 otherwise
     */
    private int sign(int x) {
        return x < 0 ? -1 : 1;
    }

    /**
     * Finds the intersection of the lines containing this and other
     * line segment. If it is not in Z^2, then null is returned.
     *
     * @param other another line segment
     * @return the point of collision between two lines
     */
    private Point2D collisionPoint(LineSegment other) {
        boolean pos = this.positiveSlope();
        int y = pos ? this.end.getY() - this.end.getX() + other.end.getY() + other.end.getX()
                : this.end.getY() + this.end.getX() + other.end.getY() - other.end.getX();
        if ((y & 1) == 1) return null;
        y >>= 1;
        return new Point2D(pos ? y - (this.end.getY() - this.end.getX())
                : y - (other.end.getY() - other.end.getX()), y);
    }
}
