import org.junit.Test;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

/**
 * Created by Jonni on 7/14/2017.
 */
public class DiamondTest {

    @Test
    public void linesTest1() {
        // |x| + |y| = 1
        //
        //      (0,1)
        // (-1,0)    (1,0)
        //      (0,-1)
        Set<LineSegment> set = new HashSet<>();
        set.addAll(new Diamond(Util.createME(0, 0, 1)).getLines());
        assertTrue(set.containsAll(Arrays.asList(
                new LineSegment(-1,0,0,1),
                new LineSegment(1,0,0,1),
                new LineSegment(0,-1,1,0),
                new LineSegment(0,-1,-1,0)
        )));
    }

    @Test
    public void linesTest2() {
        // |1000000 - x| + |1000000 - y| = 4000000
        //
        //            (1000000, 5000000)
        // (-3000000, 1000000)   (5000000, 1000000)
        //            (1000000, -3000000)
        Set<LineSegment> set = new HashSet<>();
        set.addAll(new Diamond(Util.createME(1000000, 1000000, 4000000)).getLines());
        assertTrue(set.containsAll(Arrays.asList(
                new LineSegment(-3000000,1000000,1000000,5000000),
                new LineSegment(5000000,1000000,1000000,5000000),
                new LineSegment(1000000,-3000000,5000000,1000000),
                new LineSegment(1000000,-3000000,-3000000,1000000)
        )));
    }


    @Test
    public void linesTest3() {
        // |-1000000 - x| + |1000000 - y| = 4000000
        //
        //            (-1000000, 5000000)
        // (-5000000, 1000000)   (3000000, 1000000)
        //            (-1000000, -3000000)
        Set<LineSegment> set = new HashSet<>();
        set.addAll(new Diamond(Util.createME(-1000000, 1000000, 4000000)).getLines());
        assertTrue(set.containsAll(Arrays.asList(
                new LineSegment(3000000,1000000,-1000000,5000000),
                new LineSegment(-5000000,1000000,-1000000,5000000),
                new LineSegment(-1000000,-3000000,-5000000,1000000),
                new LineSegment(-1000000,-3000000,3000000,1000000)
        )));
    }

    @Test
    public void linesTest4() {
        // |-1-x| + |-1-y| = 2
        //
        //     (-1,1)
        // (-3,-1) (1,-1)
        //     (-1,-3)
        Set<LineSegment> set = new HashSet<>();
        set.addAll(new Diamond(Util.createME(-1, -1, 2)).getLines());
        assertTrue(set.containsAll(Arrays.asList(
                new LineSegment(-3,-1,-1,1),
                new LineSegment(1,-1,-1,1),
                new LineSegment(-1,-3,-3,-1),
                new LineSegment(-1,-3,1,-1)
        )));
    }

    @Test
    public void linesTest5() {
        Diamond d = new Diamond(Util.createME(-1312415, 542513, 0));
        assertEquals(1, d.getLines().size());
        assertTrue(d.getLines().get(0).equals(new LineSegment(-1312415, 542513,-1312415, 542513)));
    }

    @Test
    public void linesTest6() {
        Diamond d = new Diamond(Util.createME(2, -1, 1));
    }
}