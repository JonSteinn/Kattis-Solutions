import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by Jonni on 6/20/2017.
 */
public class State {
    private int[] values;

    public State(int[] values) {
        this.values = values;
    }

    @Override
    public boolean equals(Object o) {
        return Arrays.equals(this.values, ((State)o).values);
    }

    @Override
    public int hashCode() {
        return Arrays.hashCode(this.values);
    }

    public boolean isGoal(Environment environment) {
        return this.values[0] == environment.getGoal();
    }

    public Map<State, Integer> getNeighbors(Environment environment) {
        Map<State, Integer> neighbors = new HashMap<>();
        for (int i = 0; i < values.length; i++) {
            for (int j = i + 1; j < values.length; j++) {
                from(environment, i, j, neighbors);
                from(environment, j, i, neighbors);
            }
        }
        return neighbors;
    }

    private void from(Environment env, int i, int j, Map<State, Integer> map) {
        if (values[i] != 0 && values[j] != env.getBoundaries()[j]) {
            int free = env.getBoundaries()[j] - values[j];
            if (values[i] > free) {
                map.put(transfer(free, i, j), free);
            } else {
                map.put(transfer(values[i], i, j), values[i]);
            }
        }
    }

    private State transfer(int amount, int i, int j) {
        int[] newArray = Arrays.copyOf(values, values.length);
        newArray[i] -= amount;
        newArray[j] += amount;
        return new State(newArray);
    }
}
