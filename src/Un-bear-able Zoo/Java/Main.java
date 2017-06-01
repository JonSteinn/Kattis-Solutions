import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        in.useLocale(Locale.US);
        int listNumber = 1;
        int n;
        while ((n = Integer.parseInt(in.nextLine())) != 0) {
            TreeMap<String, Integer> occurrences = new TreeMap<>();
            for (int i = 0; i < n; i++) {
                String animal = last(in.nextLine().split(" ")).toLowerCase();
                occurrences.putIfAbsent(animal, 0);
                occurrences.put(animal, occurrences.get(animal) + 1);
            }
            System.out.printf("List %d:\n", listNumber++);
            for (Map.Entry<String, Integer> entry : occurrences.entrySet()) {
                System.out.printf("%s | %d\n", entry.getKey(), entry.getValue());
            }
        }
    }
    private static String last(String[] arr) {
        return arr[arr.length - 1];
    }
}
