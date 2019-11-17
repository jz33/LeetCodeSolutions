'''
430. Flatten a Multilevel Doubly Linked List
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

You are given a doubly linked list which in addition to the next and previous pointers,
it could have a child pointer, which may or may not point to a separate doubly linked list.
These child lists may have one or more children of their own,
and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
You are given the head of the first level of the list.

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        '''
        Preorder traversal
        '''
        fakeHead = Node()
        grow = fakeHead
        stack = []
        while head or stack:            
            if head:
                grow.next = head
                head.prev = grow
                grow = head

                if head.child:
                    stack.append(head.next)
                    child = head.child
                    head.child = None
                    head = child
                else:
                    head = head.next
            else:
                head = stack.pop()
             
        if not fakeHead.next:
            return None
        else:
            r = fakeHead.next
            r.prev = None
            fakeHead.next = None
            return r
