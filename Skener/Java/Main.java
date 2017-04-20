/**
 * Created by Jonni on 3/1/2017.
 */
public class Main {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);
        int h = io.getInt();
        /*int w = */io.getInt();
        int dH = io.getInt();
        int dW = io.getInt();
        for (int i = 0; i < h; i++) {
            String nextRow = io.getWord().replaceAll(".", new String(new char[dW]).replace("\0", "$0"));
            for (int j = 0; j < dH; j++) io.println(nextRow);
        }
        io.close();
    }
}
