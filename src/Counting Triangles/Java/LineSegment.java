/**
 * Created by Jonni on 7/31/2017.
 */
public class LineSegment {
    public final Point p, q;
    public LineSegment(Point p, Point q) {
        this.p = p;
        this.q = q;
    }
    public boolean isPoint() {
        return p.equals(q);
    }
    public boolean intersect(LineSegment other) {
        if (this.isPoint() || other.isPoint()) return false;
        double d = ((this.q.x - this.p.x) * (other.q.y - other.p.y)) - ((this.q.y - this.p.y) * (other.q.x - other.p.x));
        if (d == 0) return false;
        double a = (((this.p.y - other.p.y) * (other.q.x - other.p.x)) - ((this.p.x - other.p.x) * (other.q.y - other.p.y))) / d;
        double b = (((this.p.y - other.p.y) * (this.q.x - this.p.x)) - ((this.p.x - other.p.x) * (this.q.y - this.p.y))) / d;
        return (a >= 0 && a <= 1) && (b >= 0 && b <= 1);
    }
}