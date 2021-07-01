package leetcode.lru146;

public class Node<T> {
    public Node<T> prev;
    public Node<T> next;
    public T data;

    @Override
    public String toString() {
        return data.toString();
    }
}
