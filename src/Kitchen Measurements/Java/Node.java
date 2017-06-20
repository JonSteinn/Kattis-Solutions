/**
 * Created by Jonni on 6/20/2017.
 */
public class Node {
    private State state;
    private Node parent;
    private int cost;

    public Node(State state, Node parent, int cost) {
        this.state = state;
        this.parent = parent;
        this.cost = cost;
    }

    public Node(State state) {
        this(state, null, 0);
    }

    public State getState() {
        return this.state;
    }

    public Node getParent() {
        return this.parent;
    }

    public int getCost() {
        return this.cost;
    }
}
