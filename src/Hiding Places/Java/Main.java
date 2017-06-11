/**
 * Created by Jonni on 6/11/2017.
 */
public class Main {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);
        int n = io.getInt();
        for (int i = 0; i < n; i++) {
            io.println(new BFS(io.getWord()));
        }
        io.close();
    }
}
