import java.util.*;

/**
 * Created by Jonni on 6/20/2017.
 */
public class Djikstra {
    private int totalCost;

    public Djikstra(Environment environment) {
        Node goal = null;
        PriorityQueue<Node> open = new PriorityQueue<>(Comparator.comparingInt(Node::getCost));
        Set<State> closed = new HashSet<>();
        open.add(new Node(new State(environment.getInit())));
        while (!open.isEmpty()) {
            Node current = open.poll();
            if (closed.contains(current.getState())) continue;
            closed.add(current.getState());
            if (current.getState().isGoal(environment)) {
                goal = current;
                break;
            }
            for (Map.Entry<State, Integer> entry : current.getState().getNeighbors(environment).entrySet()) {
                if (!closed.contains(entry.getKey())) {
                    open.add(new Node(entry.getKey(), current, current.getCost() + entry.getValue()));
                }
            }
        }
        totalCost = goal == null ? -1 : goal.getCost();
    }

    public int getTotalCost() {
        return this.totalCost;
    }
}
