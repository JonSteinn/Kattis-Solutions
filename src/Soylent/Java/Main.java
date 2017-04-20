/**
 * Created by Jonni on 3/1/2017.
 */
public class Main {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);
        int c, n = io.getInt();
        while (n-- > 0) io.println((c = io.getInt()) % 400 == 0 ? c / 400 : c / 400 + 1);
        io.close();
    }
}
