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
    def __init__(self, key = None, val = None, count = 0):
        self.key = key
        self.val = val
        self.count = count
        self.next = None
        self.prev = None
 
    def __str__(self) -> str:
        return '(' + str(self.key) + ' : ' + str(self.val) + ')'
    
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
        
class DoubleLinkedListMatrix:
    '''
    Double linked list of double linked list!
    '''
    def __init__(self):
        head = DoubleLinkedList()
        tail = DoubleLinkedList()
        head.next = tail
        tail.prev = head
        self.head = head 
        self.tail = tail
        self.countToDLL = {0 : head} # count : double linked list 
        
    def addDll(self, count: int):
        '''
        Append new dll if not existed
        '''
        if count > 0 and count not in self.countToDLL:
            dll = DoubleLinkedList()            
            prevDll = self.countToDLL[count - 1]

            # Append new dll after previous dll
            dll.next = prevDll.next
            dll.prev = prevDll
            dll.next.prev = dll
            prevDll.next = dll

            self.countToDLL[count] = dll
        
    def appendNode(self, node: Node):
        count = node.count
        if count > 0:
            dll = self.countToDLL[count]
            dll.append(node)
        
    def removeNode(self, node: Node):
        count = node.count
        if count > 0:
            dll = self.countToDLL[count]
            dll.remove(node)
            
            # Remove linked list if empty
            if dll.isEmpty():       
                dll.prev.next = dll.next
                dll.next.prev = dll.prev
                dll.next = None
                dll.prev = None
                del self.countToDLL[count]
                
    def upgradeNode(self, node: Node):
        '''
        Node must exist.
        Notice the order here. Must try add new dll first,
        as it uses count - 1 to find previous dll.
        '''
        self.addDll(node.count + 1)
        self.removeNode(node)
        node.count += 1
        self.appendNode(node)

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.matrix = DoubleLinkedListMatrix(); 
        self.keyToNode = {} # key : Node

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        
        node = self.keyToNode.get(key, None)
        if node:
            self.matrix.upgradeNode(node)
            return node.val
        
        return -1

    def put(self, key: int, val: int) -> None:
        if self.capacity == 0:
            return
        
        node = self.keyToNode.get(key, None)
        if node:          
            node.val = val
        else:
            if len(self.keyToNode) == self.capacity:
                topDll = self.matrix.head.next
                topNode = topDll.head.next
                self.matrix.removeNode(topNode)
                del self.keyToNode[topNode.key]

            node = Node(key, val, 0) # Use 0 as count will be upgraded
            self.keyToNode[key] = node

        self.matrix.upgradeNode(node)
