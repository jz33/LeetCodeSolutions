'''
705. Design HashSet
https://leetcode.com/problems/design-hashset/

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)
'''
from typing import Tuple

class Node:
    '''
    Single Linked List Node
    '''
    def __init__(self, key):
        self.key = key
        self.next = None
                    
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        An array of linked list nodes
        """
        self.map = [None] * (1 << 10)

    def hash(self, i: int) -> int:
        return i % len(self.map)
    
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

    def add(self, key: int) -> None:
        code = self.hash(key)
        head = self.map[code]
        if not head:
            self.map[code] = Node(key)
        else:
            found, node, _ = self.find(head, key)
            if not found:
                node.next = Node(key)

    def remove(self, key: int) -> None:
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

    def contains(self, key: int) -> bool:
        code = self.hash(key)
        head = self.map[code]
        if not head:
            return False
        
        found, _, _ = self.find(head, key)
        return found
