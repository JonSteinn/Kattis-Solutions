/**
 * Created by Jonni on 3/1/2017.
 */
public class Main {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);
        int n = io.getInt();
        for (int i = 0; i < n; i++) {
            int _new, _old = io.getInt(), bound = 0;
            while ((_new = io.getInt()) != 0) {
                int diff = _new - (_old << 1);
                if (diff > 0) bound += diff;
                _old = _new;
            }
            io.println(bound);
        }
        io.close();
    }
}
