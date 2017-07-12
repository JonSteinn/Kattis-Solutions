import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));

        int n = in.nextInt();
        for (int i = 0; i < n; i++) {
            int size = in.nextInt();
            Pair[] people = new Pair[size];
            for (int j = 0; j < size; j++) {
                String name = in.next();
                people[j] = new Pair(name.substring(0, name.length() - 1), in.next().split("-"));
                in.next(); // DUMP class
            }
            Arrays.sort(people);
            for (Pair p : people) out.println(p.name);
            out.println("==============================");
        }

        out.close();
    }
}