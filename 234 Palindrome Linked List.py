'''
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a
palindrome
or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

Constraints:
    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# /**
#  * Get middle node of the linked list
#  * 0->1->2->3->4 => 2
#  * 0->1->2->3 => 1
#  */
def getMiddle(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow

# /**
#  * Iterative way to reverse a linked list
#  */
def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    p0 = head
    p1 = head.next
    p0.next = None
    while p1.next:
        p2 = p1.next
        p1.next = p0
        p0 = p1
        p1 = p2
    p1.next = p0
    return p1

# /**
#  * Compare 2 linked lists from beginning if all values are identical
#  */
def compare(a: ListNode, b: ListNode) -> bool:
    pa = a
    pb = b
    while pa and pb:
        if pa.val != pb.val:
            return False
        pa = pa.next
        pb = pb.next
    return True

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        middle = getMiddle(head)
        reversedHead = reverse(middle.next)
        middle.next = None
        result = compare(head, reversedHead)
        # Recover
        middle.next = reverse(reversedHead)
        return result

