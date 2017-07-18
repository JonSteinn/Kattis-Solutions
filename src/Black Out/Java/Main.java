import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.println("5 1 5 6");
            while(sc.next().charAt(0) == 'M') {
                int r1 = sc.nextInt();
                int c1 = sc.nextInt();
                int r2 = sc.nextInt();
                int c2 = sc.nextInt();
                if (r2 == 5) r2--;
                System.out.println((5 - r2) + " " + (7 - c2) + " " + (5 - r1) + " " + (7 - c1));
            }
        }
    }
}