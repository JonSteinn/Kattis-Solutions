/**
 * Created by Jonni on 3/1/2017.
 */
public class Main {
    private static Kattio io;
    private static void evaluateNext() {
        io.print(io.getWord());
        if (Integer.parseInt(io.getWord().split("/")[0]) >= 2010) {
            io.println(" eligible");
            io.getWord();io.getWord(); //dump
        } else if (Integer.parseInt(io.getWord().split("/")[0]) >= 1991){
            io.println(" eligible");
            io.getWord();
        } else if (Integer.parseInt(io.getWord()) > 40) {
            io.println(" ineligible");
        } else {
            io.println(" coach petitions");
        }
    }
    public static void main(String[] args) {
        io = new Kattio(System.in, System.out);
        int n = io.getInt();
        for (int i = 0; i < n; i++) {
            evaluateNext();
        }
        io.close();
    }
}