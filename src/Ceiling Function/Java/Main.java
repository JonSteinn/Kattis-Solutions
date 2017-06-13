import java.io.*;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by Jonni on 6/11/2017.
 */
public class Main {
    public static void main(String[] args) {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        try {
            String[] first = in.readLine().split(" ");
            int n = Integer.parseInt(first[0]);
            Set<String> set = new HashSet<>();
            for (int i = 0; i < n; i++) {
                String[] next = in.readLine().split(" ");
                BST bst = new BST();
                for (String str : next) {
                    bst.add(Integer.parseInt(str));
                }
                set.add(bst.toString());
            }
            out.println(set.size());
        } catch (IOException e) {
            //e.printStackTrace();
        }
        out.close();
    }
}
