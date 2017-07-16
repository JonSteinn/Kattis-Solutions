import org.junit.Test;

import static org.junit.Assert.assertEquals;

/**
 * Created by Jonni on 7/14/2017.
 */
public class ManhattanEquationTest {

    @Test
    public void gettersTest() {
        ManhattanEquation eq = new ManhattanEquation(Util.equationToScanner(999999, 0, 1000));
        assertEquals("x", 999999, eq.getBeaconX());
        assertEquals("y", 0, eq.getBeaconY());
        assertEquals("d", 1000, eq.getDistance());
    }
}