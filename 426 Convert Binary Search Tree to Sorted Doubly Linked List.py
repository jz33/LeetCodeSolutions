'''
426. Convert Binary Search Tree to Sorted Doubly Linked List
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

Convert a BST to a sorted circular doubly-linked list in-place.
Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        fakeHead = Node()
        prev = fakeHead
        curr = root
        
        # Inorder
        stack = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                
                # Link
                prev.right = curr
                curr.left = prev
                
                prev = curr
                curr = curr.right
                
        # Now prev should point to last node
        head = fakeHead.right
        
        prev.right = head
        head.left = prev
        
        return head
