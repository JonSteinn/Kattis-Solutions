/**
 * Created by Jonni on 6/22/2017.
 */
public class Node {
    public Node parent;
    public int value;

    public Node(int value, Node parent) {
        this.value = value;
        this.parent = parent;
    }

    public Node(int value) {
        this(value, null);
    }
}
