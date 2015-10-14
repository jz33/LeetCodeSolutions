# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
fake->head->...->front->new_tail->....->new_head->...->None
'''
class Solution(object):
    def reverseBetween(self, head, lt, rt):
        if lt == rt: return head
        fake = ListNode(-1)
        fake.next = head
        front = fake
        i = 1
        while i < lt:
            front = front.next
            i += 1
        
        new_tail = front.next
        p = new_tail
        q = p.next
        i = lt + 1
        while i < rt:
            r = q.next
            q.next = p
            p = q
            q = r
            i += 1

        new_tail.next = q.next
        q.next = p
        front.next = q
        return fake.next
