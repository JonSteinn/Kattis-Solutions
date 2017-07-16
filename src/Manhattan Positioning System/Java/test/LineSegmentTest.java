import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by Jonni on 7/14/2017.
 */
public class LineSegmentTest {

    @Test
    public void orderTest() {
        LineSegment ls = new LineSegment(0,0, 1,1);
        assertEquals(new Point2D(0,0), ls.getOrigin());
        assertEquals(new Point2D(1,1), ls.getEnd());
        ls = new LineSegment(0,0, -1,-1);
        assertEquals(new Point2D(-1,-1), ls.getOrigin());
        assertEquals(new Point2D(0, 0), ls.getEnd());
    }

    @Test
    public void isPointTest() {
        LineSegment ls = new LineSegment(-50,50,50,-50);
        assertFalse(ls.isPoint());
        ls = new LineSegment(50, -50, 50, -50);
        assertTrue(ls.isPoint());
    }

    @Test
    public void positiveSlopeTest() {
        LineSegment ls1 = new LineSegment(0,0, 1, 1);
        LineSegment ls2 = new LineSegment(0,0, -1, -1);
        LineSegment ls3 = new LineSegment(0,0, -1, 1);
        LineSegment ls4 = new LineSegment(0,0, 1, -1);
        LineSegment ls5 = new LineSegment(-16,-2, -5555, -3);
        LineSegment ls6 = new LineSegment(-16,-2, -5555, -1);
        assertTrue(ls1.positiveSlope());
        assertTrue(ls2.positiveSlope());
        assertFalse(ls3.positiveSlope());
        assertFalse(ls4.positiveSlope());
        assertTrue(ls5.positiveSlope());
        assertFalse(ls6.positiveSlope());
    }

    @Test
    public void containsTest() {
        LineSegment ls = new LineSegment(0,-5, 10, 5);
        assertTrue(ls.contains(new Point2D(0,-5)));
        assertTrue(ls.contains(new Point2D(10,5)));
        assertTrue(ls.contains(new Point2D(1,-4)));
        assertTrue(ls.contains(new Point2D(9,4)));
        assertTrue(ls.contains(new Point2D(5,0)));
        assertFalse(ls.contains(new Point2D(-1,-6)));
        assertFalse(ls.contains(new Point2D(11,6)));

        ls = new LineSegment(0,0,5,-5);
        assertTrue(ls.contains(new Point2D(0,0)));
        assertTrue(ls.contains(new Point2D(5,-5)));
        assertTrue(ls.contains(new Point2D(1,-1)));
        assertTrue(ls.contains(new Point2D(4,-4)));
        assertFalse(ls.contains(new Point2D(-1,1)));
        assertFalse(ls.contains(new Point2D(6,-6)));
    }

    @Test
    public void stringTest() {
        assertEquals("(0,0) -> (1,1)", new LineSegment(1,1,0,0).toString());
    }

    @Test
    public void equalsTest() {
        LineSegment ls = new LineSegment(-5,3, 3, 11);
        assertTrue(ls.equals(new LineSegment(3, 11, -5, 3)));
        assertTrue(ls.equals(new LineSegment(-5, 3, 3, 11)));
        assertFalse(ls.equals(new LineSegment(-5,3, 2,10)));
        assertFalse(ls.equals(new LineSegment(3,11, -5,4)));
        assertFalse(ls.equals(new LineSegment(-5,3, 5, -7)));
    }

    @Test
    public void sameSlopeCollisionTest1() {
        LineSegment ls = new LineSegment(0,0, 5, 5);
        assertNull(ls.sameSlopeCollision(new LineSegment(6,6, 8, 8)));
        assertNull(ls.sameSlopeCollision(new LineSegment(-5,-5, -1, -1)));

        ls = new LineSegment(-5, -10, -3, -8);
        assertNull(ls.sameSlopeCollision(new LineSegment(-6,-11, -10, -15)));
        assertNull(ls.sameSlopeCollision(new LineSegment(-2,-7, 4, -1)));

        ls = new LineSegment(13, 2, 17, 6);
        assertNull(ls.sameSlopeCollision(new LineSegment(0,-11, -5, -16)));
        assertNull(ls.sameSlopeCollision(new LineSegment(19,8, 18, 7)));
    }

    @Test
    public void sameSlopeCollisionTest2() {
        LineSegment ls = new LineSegment(5,-5, 0,0);
        assertNull(ls.sameSlopeCollision(new LineSegment(-1,1, -3,3)));
        assertNull(ls.sameSlopeCollision(new LineSegment(6,-6,1000,-1000)));
    }

    @Test
    public void sameSlopeCollisionTest3() {
        LineSegment ls = new LineSegment(33, 66, 555, 555 + 33);
        assertNull(ls.sameSlopeCollision(new LineSegment(34, 66, 556, 667 + 33)));
        ls = new LineSegment(5000,0, 10000, -5000);
        assertNull(ls.sameSlopeCollision(new LineSegment(0,0, 1, -1)));
    }

    @Test
    public void sameSlopeCollisionTest4() {
        LineSegment ls = new LineSegment(-1000000,-1000000, 1000000, 1000000);
        assertEquals(new LineSegment(-1,-1,1,1),
                ls.sameSlopeCollision(new LineSegment(-1,-1,1,1)));
        assertEquals(new LineSegment(-555,-555,-555,-555),
                ls.sameSlopeCollision(new LineSegment(-555,-555,-555,-555)));
    }

    @Test
    public void sameSlopeCollisionTest5() {
        LineSegment ls = new LineSegment(-555,-333,-222,-666);
        assertEquals(new LineSegment(-300, -588, -299, -589),
                ls.sameSlopeCollision(new LineSegment(-300, -588, -299, -589)));
        assertEquals(new LineSegment(-500, -388, -500, -388),
                ls.sameSlopeCollision(new LineSegment(-500, -388 , -500, -388)));
    }

    @Test
    public void sameSlopeCollisionTest6() {
        LineSegment ls = new LineSegment(10,5, 25, 20);
        assertEquals(new LineSegment(10, 5, 25, 20),
                ls.sameSlopeCollision(new LineSegment(5,0, 30, 25)));
        assertEquals(new LineSegment(10, 5, 25, 20),
                ls.sameSlopeCollision(new LineSegment(10, 5, 25, 20)));
    }

    @Test
    public void sameSlopeCollisionTest7() {
        LineSegment ls = new LineSegment(10,-5, 25, -20);
        assertEquals(new LineSegment(10, -5, 25, -20),
                ls.sameSlopeCollision(new LineSegment(-10,15, 50, -45)));
        assertEquals(new LineSegment(10, -5, 25, -20),
                ls.sameSlopeCollision(new LineSegment(10,-5,25,-20)));
    }

    @Test
    public void sameSlopeCollisionTest8() {
        LineSegment ls = new LineSegment(-4,-5, 0, -1);
        LineSegment ls2 = new LineSegment(-7,-8, -1,-2);
        LineSegment ls3 = new LineSegment(-3, -4, 4, 3);
        LineSegment ls4 = new LineSegment(-5,-6, -4, -5);
        LineSegment ls5 = new LineSegment(0,-1,1,0);
        assertEquals(new LineSegment(-4,-5,-1,-2), ls.sameSlopeCollision(ls2));
        assertEquals(new LineSegment(-3,-4,0,-1), ls.sameSlopeCollision(ls3));
        assertEquals(new LineSegment(-4,-5,-4,-5), ls.sameSlopeCollision(ls4));
        assertEquals(new LineSegment(0,-1,0,-1), ls.sameSlopeCollision(ls5));
    }

    @Test
    public void sameSlopeCollisionTest9() {
        LineSegment ls = new LineSegment(-5,5, 5, -5);
        LineSegment ls2 = new LineSegment(0, 0, 1000000, -1000000);
        LineSegment ls3 = new LineSegment(-25, 25, -4, 4);
        LineSegment ls4 = new LineSegment(-6,6,-5,5);
        LineSegment ls5 = new LineSegment(5,-5,6,-6);
        assertEquals(new LineSegment(0,0,5,-5), ls.sameSlopeCollision(ls2));
        assertEquals(new LineSegment(-5,5,-4,4), ls.sameSlopeCollision(ls3));
        assertEquals(new LineSegment(-5,5,-5,5), ls.sameSlopeCollision(ls4));
        assertEquals(new LineSegment(5,-5,5,-5), ls.sameSlopeCollision(ls5));
    }

    @Test
    public void oppositeSlopeCollisionTest1() {
        LineSegment ls1 = new LineSegment(-1,-1,1,1);
        LineSegment ls2 = new LineSegment(-1,1,1,-1);
        assertEquals(new LineSegment(0,0,0,0), ls1.orthogonalSlopeCollision(ls2));
        assertEquals(new LineSegment(0,0,0,0), ls2.orthogonalSlopeCollision(ls1));
    }

    @Test
    public void oppositeSlopeCollisionTest2() {
        LineSegment ls1 = new LineSegment(-1,-1,1,1);
        LineSegment ls2 = new LineSegment(-1,5,1,3);
        assertNull(ls1.orthogonalSlopeCollision(ls2));
        assertNull(ls2.orthogonalSlopeCollision(ls1));
    }
    @Test
    public void oppositeSlopeCollisionTest3() {
        LineSegment ls1 = new LineSegment(-3,6,6,-3);
        LineSegment ls2 = new LineSegment(6,-3, 0, -9);
        assertEquals(new LineSegment(6,-3,6,-3), ls1.orthogonalSlopeCollision(ls2));
        assertEquals(new LineSegment(6,-3,6,-3), ls2.orthogonalSlopeCollision(ls1));
    }

    @Test
    public void oppositeSlopeCollisionTest4() {
        LineSegment ls1 = new LineSegment(0,0,5000,5000);
        LineSegment ls2 = new LineSegment(8,10, 10,8);
        LineSegment ls3 = new LineSegment(0,0,9,9);
        assertEquals(new LineSegment(9,9,9,9), ls1.orthogonalSlopeCollision(ls2));
        assertEquals(new LineSegment(9,9,9,9), ls2.orthogonalSlopeCollision(ls1));
        assertEquals(new LineSegment(9,9,9,9), ls3.orthogonalSlopeCollision(ls2));
        assertEquals(new LineSegment(9,9,9,9), ls2.orthogonalSlopeCollision(ls3));
    }

    @Test
    public void oppositeSlopeCollisionTest5() {
        LineSegment ls1 = new LineSegment(-13, 0, 0, -13);
        LineSegment ls2 = new LineSegment(13, 0, 0, -13);
        assertEquals(new LineSegment(0,-13,0,-13), ls1.orthogonalSlopeCollision(ls2));
        assertEquals(new LineSegment(0,-13,0,-13), ls2.orthogonalSlopeCollision(ls1));
    }

    @Test
    public void oppositeSlopeCollisionTest6() {
        LineSegment ls1 = new LineSegment(4,-2,6,0);
        LineSegment ls2 = new LineSegment(7,-2,5,0);
        assertNull(ls1.orthogonalSlopeCollision(ls2));
        assertNull(ls2.orthogonalSlopeCollision(ls1));
    }

    @Test
    public void oppositeSlopeCollisionTest7() {
        LineSegment ls1 = new LineSegment(-10,0,0,-10);
        LineSegment ls2 = new LineSegment(0,0,-10,-10);
        assertEquals(new LineSegment(-5,-5,-5,-5), ls1.orthogonalSlopeCollision(ls2));
        assertEquals(new LineSegment(-5,-5,-5,-5), ls2.orthogonalSlopeCollision(ls1));
    }

    @Test
    public void oppositeSlopeCollisionTest8() {
        LineSegment ls1 = new LineSegment(-10,-10,0,0);
        LineSegment ls2 = new LineSegment(0,1,1,0);
        LineSegment ls3 = new LineSegment(0,0,10,10);
        assertNull(ls1.orthogonalSlopeCollision(ls2));
        assertNull(ls2.orthogonalSlopeCollision(ls1));
        assertNull(ls2.orthogonalSlopeCollision(ls3));
        assertNull(ls3.orthogonalSlopeCollision(ls2));
    }
}