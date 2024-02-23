'''
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    Ask interviewer if n is 0 based or 1 based
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use a front pointer from head, move n steps.
        front = head
        count = 0
        for _ in range(n):
            if not front:
                break
            front = front.next
            count += 1

        if count < n:
            # This means n is larger than size of the list.
            # Do nothing
            return head

        # If front is null now, means the head is the one to remove
        if not front:
            result = head.next
            head.next = None
            return result
        
        # Use a back pointer from head. Move front and back together
        # until front pointer reaches last node.
        back = head
        while front.next is not None:
            front = front.next
            back = back.next
        
        # The back.next is the node to remove
        # Notice since n is valid, back != last node
        removal = back.next
        back.next = removal.next
        removal.next = None
        return head
