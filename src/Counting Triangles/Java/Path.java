import java.util.Arrays;

/**
 * Created by Jonni on 7/31/2017.
 */
public class Path {
    private int[] arr;

    public Path(int x, int y, int z) {
        arr = new int[]{x,y,z};
        Arrays.sort(arr);
    }

    @Override
    public String toString() {
        return arr[0] + " " + arr[1] + " " + arr[2];
    }

    @Override
    public boolean equals(Object o) {
        Path other = (Path)o;
        return this.arr[0] == other.arr[0] && this.arr[1] == other.arr[1] && this.arr[2] == other.arr[2];
    }

    @Override
    public int hashCode() {
        return 31 * arr[0] + 47 * arr[1] + 61 * arr[2];
    }
}