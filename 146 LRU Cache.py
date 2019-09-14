'''
146. LRU Cache
https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

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
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.book = dict() # key : Node
        head = Node() # head.next point to the least recently used element
        tail = Node()
        head.next = tail
        tail.prev = head
        self.head = head 
        self.tail = tail      
        
    def get(self, key: int) -> int:
        n = self.book.get(key)
        
        if not n:
            return -1
        
        # If n is not already the most recently used
        if n != self.tail.prev: 
            self.extract(n)
            self.append(n) 

        return n.val

    def put(self, key: int, value: int) -> None:
        n = self.book.get(key)
        
        if not n: # add
            n = Node(key,value) 
            
            if len(self.book) == self.capacity:
                leastUsed = self.head.next
                self.extract(leastUsed)
                del self.book[leastUsed.key]
                
            self.book[key] = n
            self.append(n)
            
        else: # update
            n.val = value

            # If n is not already the most recently used
            if n != self.tail.prev:
                self.extract(n)
                self.append(n) 
                
    def extract(self, n: Node):
        '''
        Delete node from itse parent and child
        '''
        n.prev.next = n.next
        n.next.prev = n.prev
        n.prev = None
        n.next = None
    
    def append(self, n: Node):
        '''
        Append node to tail
        '''
        self.tail.prev.next = n
        n.prev = self.tail.prev
        self.tail.prev = n
        n.next = self.tail 
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
