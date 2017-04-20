/**
 * Created by Jonni on 3/1/2017.
 */
public class Main {
    public static int adrianIndex = 0;
    public static int brunoIndex = 0;
    public static int goranIndex = 0;

    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);
        /*int n = */io.getInt(); // Dump
        String answers = io.getWord();
        int[] score = new int[3];
        for (int i = 0; i < answers.length(); i++) {
            char correct = answers.charAt(i);
            if (correct == adrianGetNext()) score[0]++;
            if (correct == brunoGetNext()) score[1]++;
            if (correct == goranGetNext()) score[2]++;
        }
        int best = Math.max(score[0], Math.max(score[1], score[2]));
        io.println(best);
        if (score[0] == best) io.println("Adrian");
        if (score[1] == best) io.println("Bruno");
        if (score[2] == best) io.println("Goran");
        io.close();
    }

    public static char adrianGetNext() {
        char next = adrianIndex == 0 ? 'A' : adrianIndex == 1 ? 'B' : 'C';
        adrianIndex = adrianIndex == 2 ? 0 : adrianIndex + 1;
        return next;
    }
    public static char brunoGetNext() {
        char next = brunoIndex == 1 ? 'A' : brunoIndex == 3 ? 'C' : 'B';
        brunoIndex = brunoIndex == 3 ? 0 : brunoIndex + 1;
        return next;
    }
    public static char goranGetNext() {
        char next = goranIndex < 2 ? 'C' : goranIndex < 4 ? 'A' : 'B';
        goranIndex = goranIndex == 5 ? 0 : goranIndex + 1;
        return next;
    }
}