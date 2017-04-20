import java.util.*;

/**
 * Created by Jonni on 3/1/2017.
 */
public class Main {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);

        int n = io.getInt();
        while (true) {
            int[] first = new int[n], second = new int[n];
            Map<Integer, Integer> indexMap = new HashMap<>();
            for (int i = 0; i < n; i++) {
                int next = io.getInt();
                indexMap.put(next, i);
                first[i] = next;
            }
            for (int i = 0; i < n; i++) {
                second[i] = io.getInt();
            }
            Arrays.sort(first);
            Arrays.sort(second);
            int[] newSecond = new int[n];
            for (int i = 0; i < n; i++) newSecond[indexMap.get(first[i])] = second[i];
            for (int i : newSecond) io.println(i);
            n = io.getInt();
            if (n == 0) break;
            else io.println();
        }
        io.close();
    }
}