'''
460. LFU Cache
https://leetcode.com/problems/lfu-cache/

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.

int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.

void put(int key, int value) Update the value of the key if present,
or inserts the key if not already present. When the cache reaches its capacity,
it should invalidate and remove the least frequently used key before inserting a new item.
For this problem, when there is a tie (i.e., two or more keys with the same frequency),
the least recently used key would be invalidated.

To determine the least frequently used key, a use counter is maintained for each key in the cache.
The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation).
The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3

Constraints:
    1 <= capacity <= 104
    0 <= key <= 105
    0 <= value <= 109
    At most 2 * 105 calls will be made to get and put.
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
