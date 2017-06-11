import java.util.*;

/**
 * Created by Jonni on 6/11/2017.
 */
public class AStar {

    private Node goal;

    public AStar(State init) {
        goal = null;
        Set<State> closed = new HashSet<>();
        PriorityQueue<Node> open = new PriorityQueue<>(Comparator.comparingInt(n -> n.F));
        Map<State, Integer> openTracker = new HashMap<>();

        open.add(new Node(init, 0));
        openTracker.put(init, 0);

        while (!open.isEmpty()) {

            Node current = open.poll();
            openTracker.remove(current.getState());
            closed.add(current.getState());

            if (current.getState().isGoalState()) {
                goal = current;
                break;
            }

            if (current.G > 10) {
                break;
            }

            for (State child : current.getState().neighbors()) {
                if (!closed.contains(child)) {
                    Integer i = openTracker.get(child);
                    if (i == null) {
                        openTracker.put(child, current.G + 1);
                        open.add(new Node(child, current.G + 1));
                    } else if (i > current.G + 1) {
                        Node newNode = new Node(child, current.G + 1);
                        open.remove(newNode);
                        open.add(newNode);
                        openTracker.put(newNode.getState(), newNode.G);
                    }
                }
            }
        }
    }

    public int shortestPath() {
        return this.goal == null ? -1 : this.goal.G;
    }
}
