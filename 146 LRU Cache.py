'''
146. LRU Cache
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value) Update the value of the key if the key exists. Otherwise,
add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
evict the least recently used key.

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

Constraints:
    1 <= capacity <= 3000
    0 <= key <= 104
    0 <= value <= 105
    At most 2 * 105 calls will be made to get and put.
'''
class Node:
    '''
    Double linked list node
    '''
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        # Head and tail are placeholders
        head = Node()
        tail = Node()
        head.next = tail
        tail.prev = head
        self.head = head 
        self.tail = tail

    def append(self, node: Node):
        node.prev = self.tail.prev
        node.prev.next = node
        node.next = self.tail
        node.next.prev = node

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNodes = {} # { key : Node }
        self.dll = DoubleLinkedList()

    def get(self, key: int) -> int:
        node = self.keyToNodes.get(key)        
        if not node:
            return -1
        self.dll.remove(node)
        self.dll.append(node) 
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.keyToNodes.get(key)
        if node:
             # update
            node.val = value
            self.dll.remove(node)
            self.dll.append(node)
        else:
            # add
            node = Node(key, value) 
            if len(self.keyToNodes) == self.capacity:
                leastUsed = self.dll.head.next
                self.dll.remove(leastUsed)
                del self.keyToNodes[leastUsed.key]
            self.keyToNodes[key] = node
            self.dll.append(node)