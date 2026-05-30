"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

  - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
  - int get(int key) Return the value of the key if the key exists, otherwise return -1.
  - void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:

  Input
  ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
  [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
  Output
  [null, null, null, 1, null, -1, null, -1, 3, 4]

  Explanation
  LRUCache lRUCache = new LRUCache(2);
  lRUCache.put(1, 1); // cache is {1=1}
  lRUCache.put(2, 2); // cache is {1=1, 2=2}
  lRUCache.get(1);    // return 1
  lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
  lRUCache.get(2);    // returns -1 (not found)
  lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
  lRUCache.get(1);    // return -1 (not found)
  lRUCache.get(3);    // return 3
  lRUCache.get(4);    // return 4


Problem Source: LeetCode

Solution -> O(1) for get and put
"""

class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, node):
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
            return

        last = self.tail
        node.prev = last
        last.next = node
        self.tail = node
    
    def remove(self, node):
        if self.head == None and self.tail == None:
            return

        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

        elif node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None 
            else:
                self.head = None

        else:
            last = node.prev
            node_next = node.next
            if last:
                last.next = node_next
            if node_next:
                node_next.prev = last
    
    def updateEnd(self, node):
        self.remove(node)
        self.append(node)

    def pop(self):
        if self.head == None:
            return None

        node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.lru_cache = {}
        self.doubleLinkedList = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key not in self.lru_cache:
            return -1

        node = self.lru_cache[key]
        self.doubleLinkedList.updateEnd(node)
        return node.val   

    def put(self, key: int, value: int) -> None:
        if key not in self.lru_cache:
            node = Node(key, value)
            if len(self.lru_cache) == self.size:
                used = self.doubleLinkedList.pop()
                self.lru_cache.pop(used.key)
            self.lru_cache[key] = node
            self.doubleLinkedList.append(node)
        else:
            node = self.lru_cache[key]
            node.val = value
            self.doubleLinkedList.updateEnd(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)