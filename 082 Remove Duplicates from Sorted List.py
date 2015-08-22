'''
82 Remove Duplicates from Sorted List
https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/
'''
def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next == None: 
        return head;
    
    fake = ListNode(0) # fake head
    fake.next = head
    p = fake
    q = fake.next
    while q != None:
        while q.next != None and q.next.val == q.val:
            q = q.next
    
        if p.next == q:
            p = p.next
        else:
            p.next = q.next
            
        q = q.next
    return fake.next
