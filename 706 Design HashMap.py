'''
706. Design HashMap
https://leetcode.com/problems/design-hashmap/

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
'''
from typing import Tuple

class Node:
    '''
    Single Linked List Node
    '''
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    '''
    Regular hash map implementation, array + linked list
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        A map of linked list nodes
        """
        self.map = [None] * (1 << 10)

    def hash(self, i: int) -> int:
        return i % len(self.map)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        code = self.hash(key)
        head = self.map[code]
        if not head:
            self.map[code] = Node(key, value)
        else:
            found, node, _ = self.find(head, key)
            if found:
                node.val = value
            else:
                node.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        code = self.hash(key)
        head = self.map[code]
        if not head:
            return -1
        
        found, node, _ = self.find(head, key)
        return node.val if found else -1
        
    def find(self, node: Node, key: int) -> Tuple[bool, Node, Node]:
        '''
        @node is not None
        Returns a pair.
        If found, return (true, node of key, parent of node of key)
        If not found, return (false, last node, parent of last node)
        '''
        parent = None
        while True:
            if node.key == key:
                return True, node, parent
            elif node.next:
                parent = node
                node = node.next
            else:
                break
        return False, node, parent
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        code = self.hash(key)
        head = self.map[code]
        if head:
            found, node, parent = self.find(head, key)
            if found:
                if not parent:
                    # key is on head
                    self.map[code] = head.next
                    head = None
                else:
                    parent.next = node.next
                    node = None
