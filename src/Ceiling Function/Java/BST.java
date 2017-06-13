/**
 * Created by Jonni on 6/13/2017.
 */
public class BST {

    private Node root;

    private static class Node {
        private int data;
        private Node left;
        private Node right;

        private Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    public BST() {
        this.root = null;
    }

    public void add(int n) {
        this.root = addHelper(root, n);
    }

    private Node addHelper(Node node, int n) {
        if (node == null) return new Node(n);
        if (node.data < n) node.right = addHelper(node.right, n);
        else node.left = addHelper(node.left, n);
        return node;
    }

    @Override
    public String toString() {
        if (root == null) return "";
        StringBuilder str = new StringBuilder();
        toStringHelper(root, str);
        return str.toString();
    }

    private void toStringHelper(Node node, StringBuilder str) {
        if (node.left != null) {
            str.append("l");
            toStringHelper(node.left, str);
        }
        str.append('x');
        if (node.right != null) {
            str.append("r");
            toStringHelper(node.right, str);
        }
    }
}
