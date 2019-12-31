'''
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappush, heappop, heapify

def lessThan(self, that) -> bool:
    return self.val < that.val
    
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = ListNode(None)
        
        # Add the comparison method to ListNode
        ListNode.__lt__ = lessThan
        
        heap = [node for node in lists if node is not None]     
        heapify(heap)
        
        p = root
        while heap:
            node = heappop(heap)
            
            p.next = node
            p = node
            
            if node.next:
                heappush(heap, node.next)
        
        return root.next
