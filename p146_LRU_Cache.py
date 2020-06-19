'''
- Leetcode problem: 146

- Difficulty: Medium

- Brief problem description:

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it
should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class DNode():
    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.head = DNode()
        self.tail = DNode()
        self.cacheMap = {}
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.pre = self.head

    def _move_to_head(self, key):
        curNode = self.cacheMap.get(key)
        if curNode is not None:
            self._remove_node(key)
            self._add_node_at_head(curNode)

    def _remove_node(self, key):
        curNode = self.cacheMap.get(key)
        if curNode:
            curNode.pre.next = curNode.next
            curNode.next.pre = curNode.pre
            del self.cacheMap[key]
            self.size -= 1

    def _add_node_at_head(self, new_node):
        new_node.pre = self.head
        new_node.next = self.head.next
        cur_next = self.head.next
        self.head.next = new_node
        cur_next.pre = new_node
        self.cacheMap[new_node.key] = new_node
        self.size += 1

    def _remove_last_node(self):
        lastNode = self.tail.pre
        if lastNode != self.head:
            self._remove_node(lastNode.key)

    def get(self, key: int) -> int:
        curNode = self.cacheMap.get(key)
        if curNode:
            self._move_to_head(curNode.key)
            return curNode.value
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.cacheMap.get(key)
        if not node:
            if self.size == self.capacity:
                self._remove_last_node()
            self._add_node_at_head(DNode(key, value))
        else:
            node.value = value
            self._move_to_head(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)