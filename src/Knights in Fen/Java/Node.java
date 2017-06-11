/**
 * Created by Jonni on 6/11/2017.
 */
public class Node {
    private State state;
    public final int G;
    public final int F;

    public Node(State state, int G) {
        this.state = state;
        this.G = G;
        this.F = G + this.state.heuristic();
    }

    public State getState() {
        return this.state;
    }

    @Override
    public int hashCode() {
        return this.state.hashCode();
    }

    @Override
    public boolean equals(Object o) {
        return this.state.equals(((Node)o).state);
    }
}
