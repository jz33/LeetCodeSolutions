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

import heapq

class HeapNode:
    def __init__(self, node: ListNode):
        self.node = node
    
    # This method is for "<", which is necessary for heap comparison
    def __lt__(self, that) -> bool:
        return self.node.val < that.node.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = ListNode(None)
        
        heap = []     
        for n in lists:
            if n:
                heapq.heappush(heap, HeapNode(n))
        
        p = root
        while len(heap) > 0:
            hn = heapq.heappop(heap)
            n = hn.node
            
            p.next = n
            p = n
            
            if n.next:
                heapq.heappush(heap, HeapNode(n.next))
        
        return root.next
