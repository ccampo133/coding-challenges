package leetcode.lru146;

public class DataItem {
    public final int key;
    public final int value;

    public DataItem(final int key, final int value) {
        this.key = key;
        this.value = value;
    }

    @Override
    public String toString() {
        return key + "=" + value;
    }
}
