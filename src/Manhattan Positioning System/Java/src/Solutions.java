import java.util.Comparator;
import java.util.HashSet;
import java.util.Set;

/**
 * A solution to a system of manhattan equations.
 */
public class Solutions {

    private Set<LineSegment> set;

    /**
     * Constructor for solution set.
     *
     * @param initial The first diamond
     */
    public Solutions(Diamond initial) {
        this.set = new HashSet<>();
        this.set.addAll(initial.getLines());
    }

    /**
     * Add another diamond to the solution set. Removing all
     * points that do not satisfy the newly added equation.
     *
     * @param d the set of points to a single equation
     */
    public void intersect(Diamond d) {
        Set<LineSegment> newSet = new HashSet<>();
        for (LineSegment ls : this.set) {
            if (ls.isPoint()) {
                checkPointCollision(newSet, d, ls);
            } else if (d.getLines().get(0).isPoint()) {
                if (ls.sameLine(d.getLines().get(0)) && ls.contains(d.getLines().get(0).getOrigin())) {
                        newSet.add(d.getLines().get(0));
                }
            } else {
                segmentCollision(d, ls, newSet);
            }
        }
        this.set = newSet;
    }

    /**
     * Check if we have ran out of points that are solutions to
     * the set of equation.
     *
     * @return true iff there are no solutions left in the set.
     */
    public boolean isEmpty() {
        return this.set.isEmpty();
    }

    /**
     * Output as Kattis requires.
     *
     * @return "impossible" if no solutions, "uncertain" if more than 1. Otherwise "x y" for the solution point.
     */
    @Override
    public String toString() {
        if (isEmpty()) return "impossible";
        Point2D first = set.iterator().next().getOrigin();
        for (LineSegment ls : this.set) {
            if (!ls.isPoint() || !ls.getOrigin().equals(first)) return "uncertain";
        }
        return String.format("%d %d", first.getX(), first.getY());
    }

    /**
     * Check collision between a point and a newly
     * added equation to the equation system.
     *
     * @param newSet replacement set
     * @param d new equation
     * @param ls a point already in the solution set
     */
    private void checkPointCollision(Set<LineSegment> newSet, Diamond d, LineSegment ls) {
        for (LineSegment x : d.getLines()) {
            if (x.isPoint()) {
                if (x.equals(ls)) {
                    newSet.add(ls);
                    return;
                }
            } else if (x.sameLine(ls) && x.contains(ls.getOrigin())) {
                newSet.add(ls);
                return;
            }
        }
    }

    /**
     * Check collision when none of the segments are singleton sets.
     *
     * @param d the newly added equation
     * @param ls a line segment already in the solution set
     * @param newSet the replacement set
     */
    private void segmentCollision(Diamond d, LineSegment ls, Set<LineSegment> newSet) {
        final boolean sl = ls.positiveSlope();
        d.getLines().sort(Comparator.comparingInt(o -> o.isPoint() ? 2 : o.positiveSlope() == sl ? 0 : 1));
        LineSegment shared;
        if ((shared = ls.sameSlopeCollision(d.getLines().get(0))) == null) {
            if ((shared = ls.sameSlopeCollision(d.getLines().get(1))) == null) {
                if ((shared = ls.orthogonalSlopeCollision(d.getLines().get(2))) != null) {
                    newSet.add(shared);
                }
                if ((shared = ls.orthogonalSlopeCollision(d.getLines().get(3))) != null) {
                    newSet.add(shared);
                }
            } else {
                newSet.add(shared);
            }
        } else {
            newSet.add(shared);
        }
    }
}
