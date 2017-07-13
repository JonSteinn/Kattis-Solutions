import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        String line = new Scanner(new BufferedReader(new InputStreamReader(System.in))).nextLine();
        out.println(first(line.length()));
        out.println(second(line.length()));
        out.println(third(line));
        out.println(second(line.length()));
        out.println(first(line.length()));
        out.close();
    }

    private static String first(int len) {
        StringBuilder str = new StringBuilder(5 + 4 * (len - 1));
        str.append("..#..");
        for (int i = 1; i < len; i++) {
            str.append(i % 3 == 2 ? ".*.." : ".#..");
        }
        return str.toString();
    }

    private static String second(int len) {
        StringBuilder str = new StringBuilder(5 + 4 * (len - 1));
        str.append(".#.#.");
        for (int i = 1; i < len; i++) {
            str.append(i % 3 == 2 ? "*.*." : "#.#.");
        }
        return str.toString();
    }

    private static String third(String line) {
        StringBuilder str = new StringBuilder(5 + 4 * (line.length() - 1));
        str.append(String.format("#.%c.#", line.charAt(0)));
        for (int i = 1; i < line.length(); i++) {
            switch (i % 3)
            {
                case 0:
                    str.append(String.format(".%c.#", line.charAt(i)));
                    break;
                case 1:
                    if (i == line.length() - 1) str.append(String.format(".%c.#", line.charAt(i)));
                    else str.append(String.format(".%c.*", line.charAt(i)));
                    break;
                default:
                    str.append(String.format(".%c.*", line.charAt(i)));
            }
        }
        return str.toString();
    }
}