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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop, heapify

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        fakeHead = ListNode(None)
        
        # Add the comparison method to ListNode
        ListNode.__lt__ = lambda this, that : this.val < that.val
        
        heap = [node for node in lists if node is not None]     
        heapify(heap)
        
        p = fakeHead
        while heap:
            node = heappop(heap)
            
            p.next = node
            p = node
            
            if node.next:
                heappush(heap, node.next)
        
        return fakeHead.next


# A more general way
class ComparableListNode:
    def __init__(self, node: ListNode):
        self.node = node
    
    def __lt__(self, that) -> bool:
        return self.node.val < that.node.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        fakeHead = ListNode()
    
        heap = [ComparableListNode(node) for node in lists if node is not None]
        heapify(heap)
        
        p = fakeHead
        while heap:
            compNode = heappop(heap)
            node = compNode.node
            
            p.next = node
            p = node
            
            if node.next:
                heappush(heap, ComparableListNode(node.next))
        
        return fakeHead.next
