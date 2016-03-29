import heapq
'''
https://leetcode.com/problems/merge-k-sorted-lists/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        head = ListNode(None)
        p = head
        for node in lists:
            if node is not None:
                heapq.heappush(heap,(node.val,node))
        while len(heap) > 0:
            _,node = heapq.heappop(heap)
            p.next = node
            p = node
            if node.next is not None:
                heapq.heappush(heap,(node.next.val,node.next))
        return head.next
