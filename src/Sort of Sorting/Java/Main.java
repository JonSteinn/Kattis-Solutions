import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);
        int n;
        boolean first = true;
        while ((n = io.getInt()) > 0) {
            if (!first) io.println();
            else first = false;
            String[] names = new String[n];
            for (int i = 0; i < n; i++) names[i] = io.getWord();
            Arrays.sort(names, Comparator.comparing(o -> o.substring(0, 2)));
            for (String name : names) io.println(name);
        }
        io.close();
    }
}
