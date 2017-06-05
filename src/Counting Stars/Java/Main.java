public class Main {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);
        int testCase = 1;
        while (io.hasMoreTokens()) {
            io.printf(String.format("Case %d: %d\n", testCase++, new Sky(io).numberOfStars()));
        }
        io.close();
    }
}