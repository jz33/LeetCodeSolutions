'''
460. LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
  When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item.
  For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency),
  the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item
since it was inserted. This number is set to zero when the item is removed.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
class Node:
    '''
    A double linked list node
    '''
    def __init__(self, key = None, value = None, count = 0):
        self.key = key
        self.value = value
        self.count = count
        self.next = None
        self.prev = None
 
    def __str__(self) -> str:
        return '(' + str(self.key) + ' : ' + str(self.value) + ')'
    
class DoubleLinkedList:
    def __init__(self):
        # Head and tail are placeholders
        head = Node()
        tail = Node()
        head.next = tail
        tail.prev = head
        self.head = head 
        self.tail = tail
        
        # A double linked list should hold all nodes with same count
        self.count = 0
        
        # The prev and next should point to other double linked list
        self.prev = None
        self.next = None
        
    def isEmpty(self) -> bool:
        return self.head.next == self.tail and self.tail.prev == self.head
    
    def __str__(self) -> str:
        arr = []
        p = self.head
        while p:
            arr.append(str(p))
            p = p.next
        return '-'.join(arr)
    
    def append(self, n: Node):
        self.tail.prev.next = n
        n.prev = self.tail.prev
        self.tail.prev = n
        n.next = self.tail
    
    def remove(self, n: Node):
        n.prev.next = n.next
        n.next.prev = n.prev
        n.prev = None
        n.next = None
        
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        # Essentially, this is double linked list matrix
        head = DoubleLinkedList()
        tail = DoubleLinkedList()
        head.next = tail
        tail.prev = head
        self.head = head 
        self.tail = tail
        
        self.keyToNode = {} # key : Node
        self.countToDLL = {0 : head} # count : double linked list 

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        
        n = self.keyToNode.get(key, None)
        if n:
            n.count += 1
            ret = n.value           
            self.upgrade(n)       
            return ret
        
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        n = self.keyToNode.get(key, None)
        if n:          
            n.count += 1
            n.value = value
        else:
            if len(self.keyToNode) == self.capacity:
                top = self.head.next.head.next;
                self.removeNode(top.count, top)

            n = Node(key, value, 1)
            
        self.upgrade(n)
            
    def upgrade(self, n: Node):
        newCount = n.count
        self.insertDLLIfNotExisted(newCount)
        self.removeNode(newCount-1, n)
        self.appendNode(newCount, n)  
    
    def insertDLLIfNotExisted(self, c: int):
        if c not in self.countToDLL:
            dll = DoubleLinkedList()            
            pdll = self.countToDLL[c-1]
            
            # Insert new dll after previous dll
            dll.next = pdll.next
            dll.prev = pdll
            dll.next.prev = dll
            pdll.next = dll
    
            self.countToDLL[c] = dll
    
    def removeNode(self, c: int, n: Node):
        if c > 0:
            dll = self.countToDLL[c] # must existed
            dll.remove(n)
            if dll.isEmpty():
                
                # Remove dll itself
                dll.prev.next = dll.next
                dll.next.prev = dll.prev
                dll.next = None
                dll.prev = None
                
                del self.countToDLL[c] # must existed
    
            del self.keyToNode[n.key]
        
    def appendNode(self, c: int, n: Node):
        if c > 0:
            dll = self.countToDLL[c] # must existed
            dll.append(n)
            
            self.keyToNode[n.key] = n


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
