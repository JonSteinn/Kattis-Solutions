import java.util.HashSet;
import java.util.Set;

/**
 * Created by Jonni on 3/1/2017.
 */
public class Main {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);
        int n = io.getInt();
        for (int i = 0; i < n; i++) {
            Set<Integer> numbers = new HashSet<>();
            int guests = io.getInt();
            for (int _i = 0; _i < guests; _i++) update(numbers, io.getInt());
            io.printf("Case #%d: %d\n", i + 1, numbers.iterator().next());
        }
        io.close();
    }
    public static void update(Set<Integer> set, int number){
        if (set.contains(number)) set.remove(number);
        else set.add(number);
    }
}