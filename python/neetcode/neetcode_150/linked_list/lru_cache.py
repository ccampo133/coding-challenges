# https://neetcode.io/problems/lru-cache
# https://leetcode.com/problems/lru-cache/description/
# LRU Cache
# Implement the Least Recently Used (LRU) cache class LRUCache. The class should
# support the following operations
#
# LRUCache(int capacity) Initialize the LRU cache of size capacity.
# int get(int key) Return the value cooresponding to the key if the key exists,
# otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the introduction of the new
# pair causes the cache to exceed its capacity, remove the least recently used
# key. A key is considered used if a get or a put operation is called on it.
#
# Ensure that get and put each run in O(1) average time complexity.
#
# Example 1:
# Input:
# ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
#
# Output:
# [null, null, 10, null, null, 20, -1]
#
# Explanation:
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 10);  // cache: {1=10}
# lRUCache.get(1);      // return 10
# lRUCache.put(2, 20);  // cache: {1=10, 2=20}
# lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
# lRUCache.get(2);      // returns 20
# lRUCache.get(1);      // return -1 (not found)
#
# Constraints:
#
# 1 <= capacity <= 100
# 0 <= key <= 1000
# 0 <= value <= 1000

from collections import deque


# QueueLRUCache is an LRU cache that uses a queue to keep track of when items
# were used. It is not the most efficient approach since the get and put
# operations are O(N). See LRUCache for a more efficient O(1) implementation.
class QueueLRUCache:
    def __init__(self, capacity: int):
        self.cap: int = capacity
        self.items: dict[int, int] = {}
        self.q: deque = deque([])

    def get(self, key: int) -> int:
        if key in self.items:
            # Move key to the back of the queue. This is O(N) because we need to
            # search the list.
            self.q.remove(key)
            self.q.append(key)
            return self.items[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            # Remove the key from the queue - we'll put it at the back later.
            # This is O(N) because we need to search the entire queue.
            self.q.remove(key)
        elif len(self.items) == self.cap:
            # Remove least recently used key
            lruk = self.q.popleft()
            self.items.pop(lruk)
        self.items[key] = value
        self.q.append(key)


def test1_queue():
    c = QueueLRUCache(2)
    c.put(1, 10)
    assert c.items == {1: 10}
    assert c.q == deque([1])

    assert c.get(1) == 10
    assert c.items == {1: 10}
    assert c.q == deque([1])

    c.put(2, 20)
    assert c.items == {1: 10, 2: 20}
    assert c.q == deque([1, 2])

    c.put(3, 30)
    assert c.items == {2: 20, 3: 30}
    assert c.q == deque([2, 3])

    assert c.get(2) == 20
    assert c.items == {2: 20, 3: 30}
    assert c.q == deque([3, 2])

    assert c.get(1) == -1
    assert c.items == {2: 20, 3: 30}
    assert c.q == deque([3, 2])


def test2_queue():
    c = QueueLRUCache(2)
    c.put(1, 10)
    assert c.items == {1: 10}
    assert c.q == deque([1])

    assert c.get(1) == 10
    assert c.items == {1: 10}
    assert c.q == deque([1])

    c.put(2, 20)
    assert c.items == {1: 10, 2: 20}
    assert c.q == deque([1, 2])

    c.put(3, 30)
    assert c.items == {2: 20, 3: 30}
    assert c.q == deque([2, 3])

    c.put(2, 10)
    assert c.items == {2: 10, 3: 30}
    assert c.q == deque([3, 2])

    assert c.get(2) == 10
    assert c.items == {2: 10, 3: 30}
    assert c.q == deque([3, 2])

    assert c.get(1) == -1
    assert c.items == {2: 10, 3: 30}
    assert c.q == deque([3, 2])


class ListNode:
    def __init__(self, key: int, val: int, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.cap: int = capacity
        self.items: dict[int, ListNode] = {}
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def _append(self, node: ListNode):
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node

    def _remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.items:
            node = self.items[key]
            # Move node to the back of the queue.
            self._remove(node)
            self._append(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self._remove(self.items[key])
        node = ListNode(key, value)
        self.items[key] = node
        self._append(node)
        if len(self.items) > self.cap:
            lru = self.left.next
            self.items.pop(lru.key)
            self._remove(lru)


def test1():
    c = LRUCache(2)
    c.put(1, 10)
    assert c.get(1) == 10
    c.put(2, 20)
    c.put(3, 30)
    assert c.get(2) == 20
    assert c.get(1) == -1
