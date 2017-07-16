import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.nio.charset.Charset;
import java.util.Locale;
import java.util.Scanner;

/**
 * Created by Jonni on 7/14/2017.
 */
public class Util {
    public static final String newLine = System.getProperty("os.name").startsWith("Win") ? "\r\n" : "\n";
    public static final String multiple = "uncertain" + Util.newLine;
    public static final String none = "impossible" + Util.newLine;
    public static String single(int x, int y) {
        return Integer.toString(x) + " " + Integer.toString(y) + Util.newLine;
    }

    public static Diamond createDiamond(int x, int y, int d) {
        return new Diamond(createME(x,y,d));
    }

    public static ManhattanEquation createME(int x, int y, int d) {
        return new ManhattanEquation(
                getStringScanner(
                        Integer.toString(x)
                                + " " + Integer.toString(y)
                                + " " + Integer.toString(d)));
    }

    public static Scanner equationToScanner(int x, int y, int d) {
        return getStringScanner(Integer.toString(x) + " " + Integer.toString(y) + " " + Integer.toString(d));
    }

    public static Scanner getStringScanner(String input) {
        Scanner s = new Scanner(new ByteArrayInputStream(input.getBytes(Charset.forName("UTF-8"))));
        s.useLocale(Locale.US);
        return s;
    }

    public static Scanner getInputFileScanner(String path) throws FileNotFoundException {
        Scanner s = new Scanner(new File(path));
        s.useLocale(Locale.US);
        return s;
    }
}
