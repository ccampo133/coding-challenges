class Node(object):
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def to_string(self):
        return str(self.key) + "=" + str(self.value)


class DoubleLinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None

    def add_front(self, node):
        if self.first is None:
            self.first = node
            self.last = node
            node.prev = None
            node.next = None
        else:
            self.add_before(self.first, node)

    def add_before(self, node, new_node):
        new_node.next = node
        # Node is the first node
        if node.prev is None:
            new_node.prev = None
            self.first = new_node
        else:
            new_node.prev = node.prev
            node.prev.next = new_node
        node.prev = new_node

    def remove(self, node):
        # This is the first node
        if node.prev is None:
            self.first = node.next
        else:
            node.prev.next = node.next
        # This is the last node
        if node.next is None:
            self.last = node.prev
        else:
            node.next.prev = node.prev
        return node

    def remove_last(self):
        return self.remove(self.last)

    def to_string(self):
        node = self.first
        s = "["
        while node is not None:
            s += node.to_string()
            if node.next is not None:
                s += ","
            node = node.next
        return s + "]"


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = DoubleLinkedList()
        self.cache = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            item = self.cache[key]
            self.queue.remove(item)
            self.queue.add_front(item)
            return item.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # Item is already in the cache. Just update its value position
        if key in self.cache:
            item = self.cache[key]
            item.value = value
            self.queue.remove(item)
            self.queue.add_front(item)
            return

        # Evict the last item
        if len(self.cache) == self.capacity:
            item_to_remove = self.queue.remove_last()
            self.cache.pop(item_to_remove.key)

        item = Node(key, value)
        self.cache[key] = item
        self.queue.add_front(item)

    def to_string(self):
        return self.queue.to_string()


if __name__ == '__main__':
    # cache = LRUCache(2)
    # cache.put(1, 1)  # cache is [1=1]
    # cache.put(2, 2)  # cache is [1=1, 2=2]
    #
    # val = cache.get(1)  # returns 1
    # assert val == 1
    #
    # cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is [1=1, 3=3]
    #
    # val = cache.get(2)  # returns -1 (not found)
    # assert val == -1
    #
    # cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is [4=4, 3=3]
    #
    # val = cache.get(1)  # returns -1 (not found)
    # assert val == -1
    #
    # val = cache.get(3)  # returns 3
    # assert val == 3
    #
    # val = cache.get(4)  # returns 4
    # assert val == 4

    # cache = LRUCache(2)
    # cache.put(1, 1)  # cache is [1=1]
    # cache.put(2, 2)  # cache is [1=1, 2=2]
    #
    # val = cache.get(1)  # returns 1
    # assert val == 1
    #
    # cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is [1=1, 3=3]
    #
    # val = cache.get(2)  # returns -1 (not found)
    # assert val == -1
    #
    # cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is [4=4, 3=3]
    #
    # val = cache.get(1)  # returns -1 (not found)
    # assert val == -1
    #
    # val = cache.get(3)  # returns 3
    # assert val == 3
    #
    # val = cache.get(4)  # returns 4
    # assert val == 4

    # cache = LRUCache(3)
    #
    # cache.put(1, 1)  # cache is [1=1]
    # print(cache.to_string())
    #
    # cache.put(2, 2)  # cache is [2=2, 1=1]
    # print(cache.to_string())
    #
    # val = cache.get(1)  # returns 1, cache is [1=1, 2=2]
    # print(cache.to_string())
    # assert val == 1
    #
    # cache.put(3, 3)  # cache is [3=3, 1=1, 2=2]
    # print(cache.to_string())
    #
    # val = cache.get(2)  # cache is [2=2, 3=3, 1=1]
    # print(cache.to_string())
    # assert val == 2
    #
    # cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is [4=4, 2=2, 3=3]
    # print(cache.to_string())
    #
    # val = cache.get(1)  # returns -1 (not found), cache is [4=4, 2=2, 3=3]
    # print(cache.to_string())
    # assert val == -1
    #
    # val = cache.get(3)  # returns 3, cache is [3=3, 4=4, 2=2]
    # print(cache.to_string())
    # assert val == 3
    #
    # val = cache.get(4)  # returns 4, cache is [4=4, 3=3, 2=2]
    # print(cache.to_string())
    # assert val == 4

    # cache = LRUCache(1)
    # cache.put(2, 1)  # cache is [2=1]
    # print(cache.to_string())
    #
    # val = cache.get(2)  # returns 1, cache is [2=1]
    # print(cache.to_string())
    # assert val == 1

    # ["LRUCache","put","put","get","put","get","put","get","get","get"]
    # [[2],[1,0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    # vals = [None]
    # cache = LRUCache(2)
    #
    # cache.put(1, 0)  # cache is [1=0]
    # vals.append(None)
    # print(cache.to_string())
    #
    # cache.put(2, 2)  # cache is [2=2, 1=0]
    # vals.append(None)
    # print(cache.to_string())
    #
    # val = cache.get(1)  # returns 0, cache is [1=0, 2=2]
    # vals.append(val)
    # print(cache.to_string())
    # assert val == 0
    #
    # cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is [3=3, 1=0]
    # vals.append(None)
    # print(cache.to_string())
    #
    # val = cache.get(2)  # returns -1, cache is [3=3, 1=0]
    # vals.append(val)
    # print(cache.to_string())
    # assert val == -1
    #
    # cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is [4=4, 3=3]
    # vals.append(None)
    # print(cache.to_string())
    #
    # val = cache.get(1)  # returns -1 (not found), cache is [4=4, 3=3]
    # vals.append(val)
    # print(cache.to_string())
    # assert val == -1
    #
    # val = cache.get(3)  # returns 3, cache is [3=3, 4=4]
    # vals.append(val)
    # print(cache.to_string())
    # assert val == 3
    #
    # val = cache.get(4)  # returns 4, cache is [4=4, 3=3]
    # vals.append(val)
    # print(cache.to_string())
    # assert val == 4
    #
    # print(vals)

    # ["LRUCache","put","get","put","get","get"]
    # [[1],[2,1],[2],[3,2],[2],[3]]
    # vals = [None]
    # cache = LRUCache(1)
    #
    # cache.put(2, 1)  # cache is [2=1]
    # vals.append(None)
    # print(cache.to_string())
    #
    # val = cache.get(2)  # returns 1, cache is [2=1]
    # vals.append(val)
    # print(cache.to_string())
    #
    # cache.put(3, 2)  # LRU key was 2, evicts key 2, cache is [3=2]
    # vals.append(None)
    # print(cache.to_string())
    #
    # val = cache.get(2)  # returns -1, cache is [3=2]
    # vals.append(val)
    # print(cache.to_string())
    #
    # val = cache.get(3)  # returns 2, cache is [3=2]
    # vals.append(val)
    # print(cache.to_string())

    # ["LRUCache","put","put","get","put","put","get"]
    # [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
    vals = [None]
    cache = LRUCache(2)

    cache.put(2, 1)  # cache is [2=1]
    vals.append(None)
    print(cache.to_string())

    cache.put(2, 2)  # cache is [2=2]
    vals.append(None)
    print(cache.to_string())

    val = cache.get(2)  # returns 1, cache is [2=2]
    vals.append(val)
    print(cache.to_string())

    cache.put(1, 1)  # cache is [1=1, 2=2]
    vals.append(None)
    print(cache.to_string())

    cache.put(4, 1)  # LRU key was 2, evicts key 2, cache is [4=1, 1=1]
    vals.append(None)
    print(cache.to_string())

    val = cache.get(2)  # returns -1, cache is [4=1, 1=1]
    vals.append(val)
    print(cache.to_string())
    print(vals)
