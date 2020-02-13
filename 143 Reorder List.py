'''
143. Reorder List
https://leetcode.com/problems/reorder-list/

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque

class Solution:
    def reorderList(self, head: ListNode) -> None:
        dq = deque()
        p = head
        while p:
            dq.append(p)
            p = p.next
        
        while len(dq) > 1:
            left = dq.popleft()
            right = dq.pop()
            left.next = right
            if dq:
                right.next = dq[0]
            else:
                right.next = None
                
        if dq:
            dq[0].next = None
            
        return head
