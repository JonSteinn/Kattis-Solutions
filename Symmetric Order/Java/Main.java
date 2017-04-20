import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/**
 * Created by Jonni on 3/1/2017.
 */
public class Main {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);

        Queue<String> queue = new LinkedList<>();
        Stack<String> stack = new Stack<>();

        int n, index = 1;
        while ((n=io.getInt()) != 0) {
            for (int i = 0; i < n; i++) {
                if ((i & 0x1) == 0x1) stack.push(io.getWord());
                else queue.add(io.getWord());
            }
            io.printf("SET %d\n", index++);
            while (!queue.isEmpty()) io.println(queue.poll());
            while (!stack.isEmpty()) io.println(stack.pop());
        }
        io.close();
    }
}
