package lru146;

// Problem 146

import java.util.HashMap;
import java.util.Map;

public class LRUCache {

    public final int capacity;
    public final Map<Integer, Node<DataItem>> cache;
    public final DoubleLinkedList<DataItem> queue;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>(capacity);
        this.queue = new DoubleLinkedList<>();
    }

    public int get(int key) {
        if (cache.containsKey(key)) {
            final Node<DataItem> node = cache.get(key);
            queue.remove(node);
            queue.addFirst(node);
            return node.data.value;
        }
        return -1;
    }

    public void put(int key, int value) {
        // Item exists in cache - just update the value and position
        if (cache.containsKey(key)) {
            final Node<DataItem> node = cache.get(key);
            node.data = new DataItem(key, value);
            queue.remove(node);
            queue.addFirst(node);
            return;
        }

        // Cache is full - evict last item
        if (cache.size() == capacity) {
            final Node<DataItem> last = queue.removeLast();
            cache.remove(last.data.key);
        }

        final Node<DataItem> node = new Node<>();
        node.data = new DataItem(key, value);
        cache.put(key, node);
        queue.addFirst(node);
    }

    @Override
    public String toString() {
        return queue.toString();
    }
}
