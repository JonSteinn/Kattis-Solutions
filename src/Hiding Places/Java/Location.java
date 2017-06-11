import java.util.HashSet;
import java.util.Set;

/**
 * Created by Jonni on 6/11/2017.
 */
public class Location {

    private static int[] movement = {-2,-1,1,2};

    public final char file;
    public final char rank;
    public Location(String pos) {
        file = pos.charAt(0);
        rank = pos.charAt(1);
    }
    public Location(char file, char rank) {
        this.file = file;
        this.rank = rank;
    }

    private boolean isValid() {
        return file >= 'a' && file <= 'h' && rank >= '1' && rank <= '8';
    }

    public Iterable<Location> neighbors() {
        Set<Location> set = new HashSet<>();
        for (int i : movement) {
            for (int j : movement) {
                if (Math.abs(i) + Math.abs(j) == 3) {
                    Location next = new Location((char)(file + i), (char)(rank + j));
                    if (next.isValid()) {
                        set.add(next);
                    }
                }
            }
        }
        return set;
    }

    @Override
    public boolean equals(Object o) {
        Location other = (Location)o;
        return this.file == other.file && this.rank == other.rank;
    }

    @Override
    public int hashCode() {
        return 31 * file + rank;
    }

    @Override
    public String toString() {
        return new String(new char[]{file,rank});
    }
}
