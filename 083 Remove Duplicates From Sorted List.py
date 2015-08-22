'''
Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
'''
def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    p = head
    while p is not None and p.next is not None:
        if p.val == p.next.val:
            p.next = p.next.next
        else:
            p = p.next
    return head
