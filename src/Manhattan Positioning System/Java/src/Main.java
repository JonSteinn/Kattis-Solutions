import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.util.Scanner;

/**
 * Starting point.
 */
public class Main {

    /**
     * Main method sets io streams to stdin and stdout and calls another method.
     *
     * @param args command line arguments
     */
    public static void main(String[] args) {
        testCase(new PrintStream(new BufferedOutputStream(System.out)),
                new Scanner(new BufferedReader(new InputStreamReader(System.in))));
    }

    /**
     * Set up this way to test entire program with custom input streams.
     *
     * @param out output stream
     * @param in input stream
     */
    public static void testCase(PrintStream out, Scanner in) {
        // Equations
        int n = in.nextInt();

        // A Manhattan equation |x-a| + |y-b| = d for given integers
        // a,b,d has integer solutions for x,y that forms a diamond.
        // We convert each such equation to a diamond and look at
        // their intersection. We start with the entire first diamond.
        Solutions sols = new Solutions(new Diamond(new ManhattanEquation(in)));

        // For each of the following n-1 equation, we convert them to diamonds
        // and find their intersection with the set as it was before. If at
        // any point the set becomes empty, we dump the remaining input.
        for (int i = 1; i < n; i++) {
            sols.intersect(new Diamond(new ManhattanEquation(in)));
            if (sols.isEmpty()) {
                while (in.hasNext()) in.next();
                break;
            }
        }
        out.println(sols);
        out.close();
    }
}