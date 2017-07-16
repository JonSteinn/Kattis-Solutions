import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

/**
 * Created by Jonni on 7/16/2017.
 */
public class SolutionsTest {
    @Test
    public void intersectTest1() {
        Solutions s = new Solutions(Util.createDiamond(444,458,2170));
        s.intersect(Util.createDiamond(-115,280,1541));
        assertFalse(s.isEmpty());
        assertEquals("uncertain", s.toString());
    }

    @Test
    public void intersectTest2() {
        Solutions s = new Solutions(Util.createDiamond(379,106,1287));
        s.intersect(Util.createDiamond(178, 440, 1170));
        assertFalse(s.isEmpty());
        assertEquals("uncertain", s.toString());
    }

    @Test
    public void intersectTest3() {
        Solutions s = new Solutions(Util.createDiamond(49,379,359));
        s.intersect(Util.createDiamond(-353, 216, 15));
        assertTrue(s.isEmpty());
        assertEquals("impossible", s.toString());
    }

    @Test
    public void intersectTest4() {
        Solutions s = new Solutions(Util.createDiamond(-19,-12,0));
        s.intersect(Util.createDiamond(23,-18,48));
        assertFalse(s.isEmpty());
        assertEquals("-19 -12", s.toString());
    }
}