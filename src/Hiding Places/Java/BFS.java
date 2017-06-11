import java.util.*;

/**
 * Created by Jonni on 6/11/2017.
 */
public class BFS {
    private Location[] locArr;
    private int maxCost;

    public BFS(String startPos) {
        Location init = new Location(startPos);
        Map<Location, Integer> closed = new HashMap<>();
        Queue<Location> open = new LinkedList<>();
        open.add(init);
        int cost = 0;
        while (closed.size() < 64) {
            Queue<Location> temp = new LinkedList<>();
            while (!open.isEmpty()) {
                Location current = open.poll();
                closed.put(current, cost);
                for (Location loc : current.neighbors()) {
                    if (!closed.containsKey(loc)) {
                        temp.add(loc);
                    }
                }
            }
            open = temp;
            cost++;
        }
        maxCost = cost - 1;

        locArr = closed.keySet().stream().filter(e -> closed.get(e) == maxCost).toArray(Location[]::new);
        Arrays.sort(locArr, (o1, o2) -> {
            int cmp = Integer.compare(o2.rank, o1.rank);
            return cmp == 0 ? Integer.compare(o1.file, o2.file) : cmp;
        });
    }

    @Override
    public String toString() {
        StringBuilder str = new StringBuilder();
        str.append(maxCost);
        for (Location loc : locArr) str.append(' ').append(loc);
        return str.toString();
    }
}
