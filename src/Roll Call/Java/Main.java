import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);
        Map<String, Integer> lastNameCounter = new HashMap<>();
        ArrayList<String[]> list = new ArrayList<>(200);
        while (io.hasMoreTokens()) {
            String[] next = new String[]{ io.getWord(), io.getWord() };
            list.add(next);
            lastNameCounter.put(next[0], 1 + lastNameCounter.getOrDefault(next[0], 0));
        }
        list.sort((o1, o2) -> {
            int cmp = o1[1].compareTo(o2[1]);
            return cmp == 0 ? o1[0].compareTo(o2[0]) : cmp;
        });
        for (String[] name : list) {
            if (lastNameCounter.get(name[0]) > 1) io.printf("%s %s\n", name[0], name[1]);
            else io.printf("%s\n", name[0]);
        }
        io.close();
    }
}
