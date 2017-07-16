import java.util.Scanner;

/**
 * Input wrapper for equation constants x_b, y_b and d
 * in the equation |x - x_b| + |y - y_b| = d.
 */
public class ManhattanEquation {

    // Variables
    private int beaconX, beaconY, distance;

    /**
     * Equation constructor.
     *
     * @param in input stream
     */
    public ManhattanEquation(Scanner in) {
        this.beaconX = in.nextInt();
        this.beaconY = in.nextInt();
        this.distance = in.nextInt();
    }

    /**
     * X-coordinate getter.
     *
     * @return x coordinate of beacon
     */
    public int getBeaconY() {
        return this.beaconY;
    }

    /**
     * Y-coordinate getter.
     *
     * @return y coordinate of beacon
     */
    public int getDistance() {
        return this.distance;
    }

    /**
     * Distance getter.
     *
     * @return distance from beacon
     */
    public int getBeaconX() {
        return this.beaconX;
    }
}
