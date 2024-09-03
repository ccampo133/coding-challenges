package linked_list

// https://leetcode.com/problems/lru-cache/

// node is a doubly linked list node.
type node struct {
	key, val   int
	prev, next *node
}

// LRUCache represents a least-recently-used cache. It is implemented using a
// doubly linked list and a map. The doubly linked list is used to maintain the
// recentness of the keys (it acts as a FIFO queue), and the map is used to
// quickly locate the keys.
type LRUCache struct {
	cap        int
	cache      map[int]*node
	head, tail *node
}

// Constructor creates a new LRUCache with the given capacity.
func Constructor(capacity int) LRUCache {
	head, tail := node{}, node{}
	head.next = &tail
	tail.prev = &head
	return LRUCache{
		cap:   capacity,
		cache: make(map[int]*node),
		head:  &head,
		tail:  &tail,
	}
}

// Get returns the value of the key if the key exists, otherwise it returns -1.
func (c *LRUCache) Get(key int) int {
	n, ok := c.cache[key]
	if !ok {
		return -1
	}
	// Move the key to the end of the list.
	c.remove(n)
	c.enqueue(n)
	return n.val
}

// Put sets the value of the key. If the key is not present, it inserts the key
// and value. If the cache is full, it removes the least-recently-used key.
func (c *LRUCache) Put(key int, value int) {
	n, ok := c.cache[key]
	if ok {
		n.val = value
		c.remove(n)
	} else {
		n = &node{key: key, val: value}
		if len(c.cache) == c.cap {
			// Remove the least-recently-used key.
			lru := c.head.next
			c.remove(lru)
			delete(c.cache, lru.key)
		}
		c.cache[key] = n
	}
	c.enqueue(n)
}

// enqueue adds a node to the end of the list.
func (c *LRUCache) enqueue(n *node) {
	left := c.tail.prev
	n.prev = left
	n.next = c.tail
	left.next = n
	c.tail.prev = n
}

// remove removes a node from the list.
func (c *LRUCache) remove(n *node) {
	left, right := n.prev, n.next
	left.next = right
	right.prev = left
	n.prev, n.next = nil, nil
}
