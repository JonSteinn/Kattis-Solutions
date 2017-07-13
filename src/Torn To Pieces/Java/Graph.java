import java.util.*;

/**
 * Created by Jonni on 7/13/2017.
 */
public class Graph {
    private Map<String, Set<String>> edges;

    public Graph(int n, Scanner in) {
        this.edges = new HashMap<>(47);
        for (int v = 0; v < n; v++) {
            String[] line = in.nextLine().split(" ");
            if (line.length > 1) {
                this.edges.putIfAbsent(line[0], new HashSet<>(47));
                for (int i = 1; i < line.length; i++) {
                    this.edges.putIfAbsent(line[i], new HashSet<>(47));
                    this.edges.get(line[0]).add(line[i]);
                    this.edges.get(line[i]).add(line[0]);
                }
            }
        }
    }

    public Iterable<String> neighbors(String vertex) {
        return this.edges.getOrDefault(vertex, new HashSet<>());
    }

    public int numberOfVertices() {
        return this.edges.size();
    }
}
