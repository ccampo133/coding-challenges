# This is slow because it uses a queue, which requires linear time removal
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = []
        self.cache = {}

    # This is slow O(n)
    def remove_from_queue(self, key):
        if key in self.queue:
            self.queue.remove(key)

    def add_to_queue(self, key):
        self.queue.insert(0, key)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove_from_queue(key)
            self.add_to_queue(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # Item is already in the cache. Just update its value and position
        if key in self.cache:
            self.cache[key] = value
            self.remove_from_queue(key)
            self.add_to_queue(key)
            return

        # Evict the last item
        if len(self.cache) == self.capacity:
            key_to_remove = self.queue.pop()
            self.cache.pop(key_to_remove)

        self.cache[key] = value
        self.add_to_queue(key)


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

    cache = LRUCache(1)
    cache.put(2, 1)  # cache is [2=1]
    print(cache.to_string())

    val = cache.get(2)  # returns 1, cache is [2=1]
    print(cache.to_string())

    assert val == 1
