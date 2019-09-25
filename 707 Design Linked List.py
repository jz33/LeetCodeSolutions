'''
707. Design Linked List
https://leetcode.com/problems/design-linked-list/

# Test cases are wrong! Not clear if negative index should be supported
'''
class Node:
    '''
    Double Linked List Node
    '''
    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.prev = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Use 2 dummy nodes to cover boundaries
        head = Node()
        tail = Node()
        head.next = tail
        tail.prev = head
        self.head = head
        self.tail = tail

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        tag = self.getNodeAtIndex(index)
        if not tag or tag == self.tail or tag == self.head:
            return -1
        return tag.val
    
    def getNodeAtIndex(self, index: int) -> Node:
        if index >= 0:
            p = self.head
            for _ in range(index + 1):
                p = p.next
                if not p:
                    break 
            return p
        else:
            p = self.tail
            for _ in range(0, index, -1):
                p = p.prev
                if not p:
                    break
            return p

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addNodeAfter(Node(val), self.head)       

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addNodeBefore(Node(val), self.tail)
    
    def addNodeAfter(self, a: Node, b: Node):
        '''
        Add node a after node b
        '''
        a.next = b.next
        a.prev = b
        b.next = a
        a.next.prev = a
    
    def addNodeBefore(self, a: Node, b: Node):
        '''
        Add node a before node b
        '''
        self.addNodeAfter(a, b.prev)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        tag = self.getNodeAtIndex(index)
        if tag:
            if tag != self.tail and tag != self.head:
                self.addNodeBefore(Node(val), tag)
            elif index >= 0 and tag == self.tail:
                self.addAtTail(val)
            elif index < 0 and tag == self.head:
                self.addAtHead(val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        tag = self.getNodeAtIndex(index)
        if tag and tag != self.tail and tag != self.head:
            tag.prev.next = tag.next
            tag.next.prev = tag.prev
            tag.prev = None
            tag.next = None
            tag = None
