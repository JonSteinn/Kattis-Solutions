import java.util.Arrays;

/**
 * Created by Jonni on 7/12/2017.
 */
public class Pair implements Comparable<Pair> {
    public final String name;
    private String compareString;

    public Pair(String name, String[] c) {
        this.name = name;
        char[] tmp = new char[10];
        for (int i = 0; i < c.length; i++) tmp[i] = toNumber(c[c.length - i - 1]);
        for (int i = c.length; i < 10; i++) tmp[i] = '1';
        this.compareString = new String(tmp);
    }

    private char toNumber(String s) {
        return s.charAt(0) == 'u' ? '0' : s.charAt(0) == 'm' ? '1' : '2';
    }

    @Override
    public int compareTo(Pair o) {
        int x = this.compareString.compareTo(o.compareString);
        return x == 0 ? this.name.compareTo(o.name) : x;
    }
}