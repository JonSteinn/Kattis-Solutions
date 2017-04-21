/**
 * Created by Jonni on 4/18/2017.
 */
public class Main {
    public static void main(String[] args) {

        Kattio io = new Kattio(System.in, System.out);
        int r = io.getInt(), c = io.getInt();
        String least = null;
        String[] rows = new String[r];
        for (int i = 0; i < r; i++) {
            rows[i] = io.getWord();
            for (String s : rows[i].split("#")) {
                if (s.length() > 1 && (least == null || s.compareTo(least) < 0)) least = s;
            }
        }
        char[] verticals = new char[r];
        for (int i = 0; i < c; i++) {
            for (int j = 0; j < r; j++) {
                verticals[j] = rows[j].charAt(i);
            }
            for (String s : new String(verticals).split("#")) {
                if (s.length() > 1 && (least == null || s.compareTo(least) < 0)) least = s;
            }
        }
        io.println(least);
        io.close();
    }
}


/*
// a functional approach

import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);
        int r = io.getInt(), c = io.getInt();
        PriorityQueue<String> pq = new PriorityQueue<>(String::compareTo);
        String[] rows = new String[r];
        for (int i = 0; i < r; i++) {
            pq.addAll(Arrays.stream((rows[i] = io.getWord()).split("#")).filter(s -> s.length() > 1).collect(Collectors.toList()));
        }
        char[] verticals = new char[r];
        for (int i = 0; i < c; i++) {
            for (int j = 0; j < r; j++) {
                verticals[j] = rows[j].charAt(i);
            }
            pq.addAll(Arrays.stream(new String(verticals).split("#")).filter(s -> s.length() > 1).collect(Collectors.toList()));
        }
        io.println(pq.poll());
        io.close();
    }
}
*/