import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

/**
 * Created by Jonni on 7/13/2017.
 */
public class Point2DTest {

    @Test
    public void gettersTest() {
        Point2D p = new Point2D(1,2);
        assertEquals("x", 1, p.getX());
        assertEquals("y", 2, p.getY());
    }

    @Test
    public void equalsTest() {
        Point2D pnt = new Point2D(-1, 5);
        assertTrue(pnt.equals(new Point2D(-1, 5)));
        assertFalse(pnt.equals(new Point2D(-1, -5)));
        assertFalse(pnt.equals(new Point2D(1, -5)));
        assertFalse(pnt.equals(new Point2D(123, -12351)));
    }

    @Test
    public void compareTest() {
        Point2D pnt = new Point2D(0,0);
        assertTrue(pnt.compareTo(new Point2D(0,1)) < 0);
        assertTrue(pnt.compareTo(new Point2D(1, 0)) < 0);
        assertTrue(pnt.compareTo(new Point2D(-1, 1)) < 0);
        assertTrue(pnt.compareTo(new Point2D(0,0)) == 0);
        assertTrue(pnt.compareTo(new Point2D(0,-1)) > 0);
        assertTrue(pnt.compareTo(new Point2D(-1,0)) > 0);
        assertTrue(pnt.compareTo(new Point2D(1,-1)) > 0);
        assertTrue(new Point2D(-5,-5).compareTo(new Point2D(-2,-2)) < 0);
    }

    @Test
    public void StringTest() {
        assertEquals("(1,-5)", new Point2D(1,-5).toString());
    }
}