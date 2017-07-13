import java.util.*;

/**
 * Created by Jonni on 7/13/2017.
 */
public class BreadthFirstSearch {

    private Map<String, String> parents;
    private String goal;

    public BreadthFirstSearch(Graph g, String from, String to) {
        this.parents = new HashMap<>((int)(g.numberOfVertices() / 0.7));
        this.goal = null;
        this.search(g, from, to);
    }

    private void search(Graph g, String from, String to) {
        Set<String> visited = new HashSet<>(47);
        Queue<Node> frontier = new LinkedList<>();
        frontier.add(new Node(from, ""));

        while (!frontier.isEmpty()) {
            Node current = frontier.poll();
            if (!visited.contains(current.state)) {
                visited.add(current.state);
                this.parents.put(current.state, current.parent);
                for (String neighbor : g.neighbors(current.state)) {
                    if (!visited.contains(neighbor)) {
                        if (neighbor.equals(to)) {
                            this.parents.put(neighbor, current.state);
                            this.goal = neighbor;
                            return;
                        }
                        frontier.add(new Node(neighbor, current.state));
                    }
                }
            }
        }
    }

    @Override
    public String toString() {
        if (this.goal == null) return "no route found";
        Stack<String> path = new Stack<>();
        String it = this.goal;
        while (it.length() > 0) {
            path.push(it);
            it = parents.get(it);
        }
        StringBuilder str = new StringBuilder(this.parents.size());
        str.append(path.pop());
        while (!path.isEmpty()) {
            str.append(' ').append(path.pop());
        }
        return str.toString();
    }
}
