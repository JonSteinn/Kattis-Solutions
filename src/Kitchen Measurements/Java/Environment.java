import java.io.BufferedReader;
import java.io.IOException;

/**
 * Created by Jonni on 6/20/2017.
 */
public class Environment {

    private int goal;
    private int[] boundaries;
    private int[] init;
    private int length;

    public Environment(BufferedReader in) {
        try {
            String[] input = in.readLine().split(" ");
            this.length = Integer.parseInt(input[0]);
            this.init = new int[this.length];
            this.boundaries = new int[this.length];
            for (int i = 0; i < length; i++) {
                this.boundaries[i] = Integer.parseInt(input[i + 1]);
            }
            this.goal = Integer.parseInt(input[input.length - 1]);
            this.init[0] = this.boundaries[0];
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public int getGoal() {
        return this.goal;
    }

    public int[] getBoundaries() {
        return this.boundaries;
    }

    public int[] getInit() {
        return this.init;
    }

    public int getLength() {
        return this.length;
    }
}
