# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: 
            return head
        p = head
        q = p.next

        while q != None:
            if q.val < p.val:
                p.next = q.next

                if q.val < head.val:
                    q.next = head
                    head = q
                else:
                    lt = head
                    rt = lt.next

                    while lt != q:
                        if q.val < rt.val:
                            lt.next = q
                            q.next = rt
                            break
                        else:
                            lt = rt
                            rt = rt.next
                q = p.next
            else:
                p = q
                q = q.next
        return head
