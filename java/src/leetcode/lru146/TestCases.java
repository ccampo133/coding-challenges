package leetcode.lru146;

public class TestCases {

    public static void main(String[] args) {

        //["LRUCache","put","put","get","put","get","put","get","get","get"]
        //[[2],[1,0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
        LRUCache cache = new LRUCache(2);

        cache.put(1, 0); // Cache is [1=0]
        System.out.println(cache);

        cache.put(2, 2); // Cache is [2=2, 1=0]
        System.out.println(cache);

        int val = cache.get(1); // Returns 0, cache is [1=0, 2=2]
        assertEquals(0, val);
        System.out.println(cache);

        cache.put(3, 3); // LRU key is 2, evicted 2, cache is [3=3, 1=0]
        System.out.println(cache);

        val = cache.get(2); // Return's -1, cache is [3=3, 1=0]
        assertEquals(-1, val);
        System.out.println(cache);

        cache.put(4, 4); // LRU key is 1, evicted 1, cache is [4=4, 3=3]
        System.out.println(cache);

        val = cache.get(1); // Returns -1, cache is [4=4, 3=3]
        assertEquals(-1, val);
        System.out.println(cache);

        val = cache.get(3); // Returns 3, cache is [3=3, 4=4]
        assertEquals(3, val);
        System.out.println(cache);

        val = cache.get(4); // Returns 4, cache is [4=4, 3=3]
        assertEquals(4, val);
        System.out.println(cache);
    }

    public static void assertEquals(int expected, int actual) {
        if (expected != actual) {
            throw new AssertionError("Expected: " + expected + ", Actual: " + actual);
        }
    }
}
