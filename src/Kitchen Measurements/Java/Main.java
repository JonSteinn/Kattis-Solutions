import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;

/**
 * Created by Jonni on 6/11/2017.
 */
public class Main {
    public static void main(String[] args) {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        int cost = new Djikstra(new Environment(in)).getTotalCost();
        out.println(cost < 0 ? "impossible" : cost);
        out.close();
    }
}
