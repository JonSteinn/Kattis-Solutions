import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        try {
            Node[] nodes = new Node[101];
            for (int i = 1; i < 101; i++) nodes[i] = new Node(i);
            Node current = nodes[Integer.parseInt(in.readLine())];
            while(true) {
                int[] values = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                int parent = values[0];
                if (parent == -1) break;
                for (int i = 1; i < values.length; i++) nodes[values[i]].parent = nodes[parent];
            }
            StringBuilder str = new StringBuilder();
            str.append(Integer.toString(current.value));
            current = current.parent;
            while (current != null) {
                str.append(' ').append(Integer.toString(current.value));
                current = current.parent;
            }
            out.println(str.toString());
        } catch (IOException e) {
            e.printStackTrace();
        }
        out.close();
    }
}
