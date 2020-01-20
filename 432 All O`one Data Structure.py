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
class Node:
    '''
    A double linked list node.
    One node contains keys with same count
    '''
    def __init__(self, count: int):
        self.count = count
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
          
class DoubleLinkedList:
    def __init__(self):
        # Head and tail are placeholders
        head = Node(0)
        tail = Node(0)
        head.next = tail
        tail.prev = head
        self.head = head 
        self.tail = tail
        
    def insertAfter(self, pn: Node, n: Node):
        # Insert n after pn
        n.next = pn.next
        n.prev = pn
        pn.next.prev = n
        pn.next = n
        
    def insertBefore(self, pn: Node, n: Node):
        self.insertAfter(pn.prev, n)       
        
    def remove(self, n: Node):
        # Remove node n
        n.prev.next = n.next
        n.next.prev = n.prev
        n.prev = None
        n.next = None

class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dll = DoubleLinkedList()
        self.keyToNode = {} # {key : node}
        
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        n = self.keyToNode.get(key, None)
        if n is not None:
            n.remove(key)
            self.addToNextNode(key, n)
        else:
            self.addToNextNode(key, self.dll.head)
                   
    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        n = self.keyToNode.get(key, None)
        if n is not None:
            n.remove(key)
            self.addToPrevNode(key, n)
    
    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        p = self.dll.tail.prev
        while p is not None:
            if not p.isEmpty():
                return p.get()
            p = p.prev
        return ''
        
    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        p = self.dll.head.next
        while p is not None:
            if not p.isEmpty():
                return p.get()
            p = p.next
        return ''

    def addToNextNode(self, key: str, currentNode: Node):
        nextNode = currentNode.next
        if nextNode.count != currentNode.count + 1:
            nextNode = Node(currentNode.count + 1)
            self.dll.insertAfter(currentNode, nextNode)

        nextNode.add(key)
        self.keyToNode[key] = nextNode

    def addToPrevNode(self, key: str, currentNode: Node):
        if currentNode.count != 1:
            prevNode = currentNode.prev
            if prevNode.count != currentNode.count - 1:
                prevNode = Node(currentNode.count - 1)
                self.dll.insertBefore(currentNode, prevNode)

            prevNode.add(key)
            self.keyToNode[key] = prevNode
        else:
            del self.keyToNode[key]
