import org.junit.Test;

import java.io.FileNotFoundException;

import static org.junit.Assert.assertEquals;

/**
 * Created by Jonni on 7/14/2017.
 */
public class MainTest {

    private String fileName(int n) {
        return "test/test_in/" + (n < 10 ? String.format("0%d", n) : Integer.toString(n)) + ".in";
    }

    @Test
    public void completeTest1() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(1)));
        assertEquals(Util.single(1000200, 799), out.getOutput());
    }

    @Test
    public void completeTest2() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(2)));
        assertEquals(Util.multiple, out.getOutput());
    }

    @Test
    public void completeTest3() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(3)));
        assertEquals(Util.none, out.getOutput());
    }

    @Test
    public void completeTest4() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(4)));
        assertEquals(Util.none, out.getOutput());
    }

    @Test
    public void completeTest5() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(5)));
        assertEquals(Util.multiple, out.getOutput());
    }

    @Test
    public void completeTest6() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(6)));
        assertEquals(Util.none, out.getOutput());
    }

    @Test
    public void completeTest7() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(7)));
        assertEquals(Util.single(-1, 1), out.getOutput());
    }

    @Test
    public void completeTest8() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(8)));
        assertEquals(Util.single(-15555, 112333), out.getOutput());
    }

    @Test
    public void completeTest9() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(9)));
        assertEquals(Util.single(0, 0), out.getOutput());
    }

    @Test
    public void completeTest10() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(10)));
        assertEquals(Util.single(2, -21), out.getOutput());
    }

    @Test
    public void completeTest11() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(11)));
        assertEquals(Util.single(-4, -22), out.getOutput());
    }

    @Test
    public void completeTest12() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(12)));
        assertEquals(Util.multiple, out.getOutput());
    }

    @Test
    public void completeTest13() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(13)));
        assertEquals(Util.none, out.getOutput());
    }

    @Test
    public void completeTest14() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(14)));
        assertEquals(Util.multiple, out.getOutput());
    }

    @Test
    public void completeTest15() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(15)));
        assertEquals(Util.none, out.getOutput());
    }

    @Test
    public void completeTest16() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(16)));
        assertEquals(Util.single(-177, -414), out.getOutput());
    }

    @Test
    public void completeTest17() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(17)));
        assertEquals(Util.multiple, out.getOutput());
    }

    @Test
    public void completeTest18() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(18)));
        assertEquals(Util.single(0, 1), out.getOutput());
    }

    @Test
    public void completeTest19() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(19)));
        assertEquals(Util.single(0, 0), out.getOutput());
    }

    @Test
    public void completeTest20() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(20)));
        assertEquals(Util.single(1, -1), out.getOutput());
    }

    @Test
    public void completeTest21() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(21)));
        assertEquals(Util.multiple, out.getOutput());
    }

    @Test
    public void completeTest22() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(22)));
        assertEquals(Util.single(0,-1), out.getOutput());
    }

    @Test
    public void completeTest23() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(23)));
        assertEquals(Util.multiple, out.getOutput());
    }

    @Test
    public void completeTest24() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(24)));
        assertEquals(Util.single(-2, 2), out.getOutput());
    }

    @Test
    public void completeTest25() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(25)));
        assertEquals(Util.none, out.getOutput());
    }

    @Test
    public void completeTest26() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(26)));
        assertEquals(Util.none, out.getOutput());
    }

    @Test
    public void completeTest27() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(27)));
        assertEquals(Util.single(-2,2), out.getOutput());
    }

    @Test
    public void completeTest28() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(28)));
        assertEquals(Util.single(1,-2), out.getOutput());
    }

    @Test
    public void completeTest29() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(29)));
        assertEquals(Util.single(-18,4), out.getOutput());
    }

    @Test
    public void completeTest30() throws FileNotFoundException {
        OutRedirect out = new OutRedirect();
        Main.testCase(out.getStream(), Util.getInputFileScanner(fileName(30)));
        assertEquals(Util.multiple, out.getOutput());
    }
}