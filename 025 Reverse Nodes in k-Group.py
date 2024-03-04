'''
25. Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
def reverse(head: ListNode, tail: Optional[ListNode]):
    '''
    Reverse from head (inclusive) till tail (exclusive)
    '''
    if head == tail or head.next == tail:
        return head
        
    p0 = head.next
    head.next = None
    
    while p0.next != tail:
        p1 = p0.next
        p0.next = head
        head = p0
        p0 = p1
    
    p0.next = head
    return p0
    
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fakeHead = ListNode(next=head)
        prevEnd = fakeHead # end node of previous section
        tail = head
        
        while tail:
            # Try find a k group
            count = 0
            while tail and count < k:
                tail = tail.next
                count += 1
            
            if count == k:
                oldHead = prevEnd.next
                prevEnd.next = reverse(oldHead, tail)
                prevEnd = oldHead
                oldHead.next = tail

        return fakeHead.next


