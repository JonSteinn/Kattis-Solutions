import java.util.Locale;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        in.useLocale(Locale.US);
        while (in.hasNextLine()) {
            StringBuilder name = new StringBuilder();
            double sum = 0;
            int numbers = 0;
            for (String s : in.nextLine().split(" ")) {
                try {
                    double next = Double.parseDouble(s);
                    sum += next;
                    numbers++;
                } catch (NumberFormatException ex) {
                    name.append(s).append(" ");
                }
            }
            System.out.printf("%.3f %s\n", sum / numbers, name.substring(0, name.length() - 1));
        }
    }
}