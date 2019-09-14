'''
432. All O`one Data Structure
https://leetcode.com/problems/all-oone-data-structure/

Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. 
  If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
'''
from collections import defaultdict

class Node:
    '''
    A double linked list node
    '''
    def __init__(self):
        self.keys = set()
        self.next = None
        self.prev = None
    
    def add(self, key: str):
        self.keys.add(key)
    
    def remove(self, key: str):
        self.keys.remove(key)
        
    def get(self) -> str:
        for e in self.keys:
            return e
        
    def isEmpty(self) -> bool:
        return len(self.keys) == 0
    
    def __str__(self) -> str:
        return '(' + ' '.join(list(self.keys)) + ')'
          
class DoubleLinkedList:
    def __init__(self):
        # Head and tail are placeholders
        head = Node()
        tail = Node()
        head.next = tail
        tail.prev = head
        self.head = head 
        self.tail = tail
        
    def insertAfter(self, pn: Node, n: Node):
        n.next = pn.next
        n.prev = pn
        pn.next.prev = n
        pn.next = n
        
    def insertBefore(self, pn: Node, n: Node):
        self.insertAfter(pn.prev, n)       
        
    def remove(self, n: Node):
        n.prev.next = n.next
        n.next.prev = n.prev
        n.prev = None
        n.next = None
        
    def __str__(self) -> str:
        arr = []
        p = self.head
        while p:
            arr.append(str(p))
            p = p.next
        return '-'.join(arr)
                
class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dll = DoubleLinkedList()
        self.keyToCount = defaultdict(int) # key : count
        self.countToNode = {0 : self.dll.head} # count : node
        
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        pc = self.keyToCount.get(key, 0) # previous count
        cc = pc + 1 # current count
        
        # Insert node
        self.insertNodeIfNotExisted(pc, cc)
            
         # Remove previous key
        self.removeKey(key, pc)
        
        # Add current key
        self.addKey(key, cc)
                   
    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        pc = self.keyToCount.get(key, 0) # previous count
        if pc > 0:
            cc = pc - 1
            
            # Insert node
            self.insertNodeIfNotExisted(pc, cc)
                             
            # Remove previous key
            self.removeKey(key, pc)
            
            # Add current key
            self.addKey(key, cc)         

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        real_tail = self.dll.tail.prev
        if not real_tail.isEmpty():
            return real_tail.get()
        return ''
        
    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        real_head = self.dll.head.next
        if not real_head.isEmpty():
            return real_head.get()       
        return ''
       
    def insertNodeIfNotExisted(self, pc: int, cc: int):
        if cc not in self.countToNode:
            n = Node()
            
            # Notice the trick here, why there is head node inside countToNode,
            # therefore previous node must exist
            pn = self.countToNode[pc]
            
            if pc < cc:                
                self.dll.insertAfter(pn, n)
            else:
                self.dll.insertBefore(pn, n)
    
            self.countToNode[cc] = n
        
    def addKey(self, key: str, c: int):
        # Do not add key to head node
        if c > 0:
            n = self.countToNode[c] # must existed
            n.add(key)
            self.keyToCount[key] = c
              
    def removeKey(self, key: str, c: int):
        # Do not remove head node
        if c > 0:
            n = self.countToNode[c] # must existed
            n.remove(key)
            if n.isEmpty():
                self.dll.remove(n)
                del self.countToNode[c]
            del self.keyToCount[key]

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
