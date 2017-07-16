import java.util.ArrayList;
import java.util.Arrays;

/**
 * The diamond that forms the solution set for a given Manhattan equation.
 */
public class Diamond {

    // Each solution has 1 point or 4 line segments for solutions
    private ArrayList<LineSegment> lines;

    /**
     * Diamond constructor.
     *
     * @param eq a manhattan equation |a-x| + |b-y| = c where a,b,c are constants
     */
    public Diamond(ManhattanEquation eq) {
        if (eq.getDistance() == 0) {
            this.lines = new ArrayList<>();
            this.lines.add(new LineSegment(eq.getBeaconX(), eq.getBeaconY(), eq.getBeaconX(), eq.getBeaconY()));
        } else {
            int[] x = {eq.getBeaconX() - eq.getDistance(), eq.getBeaconX() + eq.getDistance(), eq.getBeaconX()};
            int[] y = {eq.getBeaconY() - eq.getDistance(), eq.getBeaconY() + eq.getDistance(), eq.getBeaconY()};
            this.lines = new ArrayList<>(Arrays.asList(
                    new LineSegment(x[0], y[2], x[2], y[0]),
                    new LineSegment(x[0], y[2], x[2], y[1]),
                    new LineSegment(x[1], y[2], x[2], y[0]),
                    new LineSegment(x[1], y[2], x[2], y[1])));
        }
    }

    /**
     * Lines getter.
     *
     * @return a set of points obtained from a manhattan equation
     */
    public ArrayList<LineSegment> getLines() {
        return this.lines;
    }
}
