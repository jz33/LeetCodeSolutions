'''
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists,
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:
    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop, heapify

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Add the comparison method to ListNode
        ListNode.__lt__ = lambda this, that : this.val < that.val
        
        heap = [node for node in lists if node is not None]     
        heapify(heap)
        
        fakeHead = ListNode(None)
        curr = fakeHead
        while heap:
            node = heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(heap, node.next)
        
        return fakeHead.next


# An old school way
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
