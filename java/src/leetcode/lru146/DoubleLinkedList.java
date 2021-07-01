package leetcode.lru146;

public class DoubleLinkedList<T> {
    private Node<T> first = null;
    private Node<T> last = null;

    public void addFirst(Node<T> node) {
        node.prev = null;
        node.next = first;

        if (first != null) {
            first.prev = node;
        }

        first = node;
        if (last == null) {
            last = node;
        }
    }

    public Node<T> remove(Node<T> node) {
        // Last node
        if (node.next == null) {
            last = node.prev;
        } else {
            node.next.prev = node.prev;
        }

        // First node
        if (node.prev == null) {
            first = node.next;
        } else {
            node.prev.next = node.next;
        }

        node.next = null;
        node.prev = null;

        return node;
    }

    public Node<T> removeLast() {
        return remove(last);
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("[");
        Node<T> node = first;
        while (node != null) {
            sb.append(node);
            if (node.next != null) {
                sb.append(",");
            }
            node = node.next;
        }
        sb.append("]");
        return sb.toString();
    }
}
