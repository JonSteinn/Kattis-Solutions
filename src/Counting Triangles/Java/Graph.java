import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

/**
 * Created by Jonni on 7/31/2017.
 */
public class Graph {
    private ArrayList<LineSegment> segments;
    private ArrayList<Set<Integer>> edges;
    private int V;
    private int triangles;

    public Graph(int V, Scanner in) {
        this.V = V;
        this.triangles = -1;
        this.edges = new ArrayList<>(V);
        this.segments = new ArrayList<>(V);
        for (int i = 0; i < V; i++) addNext(in);
        this.triangles = uniqueThreeCycles();
    }

    public int getTriangles() {
        return triangles;
    }

    private void addNext(Scanner in) {
        LineSegment next = new LineSegment(
                new Point(in.nextDouble(), in.nextDouble()),
                new Point(in.nextDouble(), in.nextDouble())
        );
        this.segments.add(next);
        this.edges.add(new HashSet<>(V));
        int currentIndex = this.segments.size() - 1;
        for (int i = 0; i < currentIndex; i++) {
            if (next.intersect(segments.get(i))) {
                this.edges.get(currentIndex).add(i);
                this.edges.get(i).add(currentIndex);
            }
        }
    }

    private int uniqueThreeCycles() {
        Set<Path> total = new HashSet<>(V * V);
        for (int a = 0; a < V; a++) {
            for (int b : this.edges.get(a)) {
                for (int c : this.edges.get(b)) {
                    if (this.edges.get(c).contains(a)) {
                        total.add(new Path(a,b,c));
                    }
                }
            }
        }
        return total.size();
    }
}