'''
285 Inorder Successor in BST

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # The successor of p is its right node's leftmost node
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        # Or its parent or ancestor
        else:         
            successor = None
            while root.val != p.val:
                if root.val > p.val:
                    successor = root
                    root = root.left
                else:
                    root = root.right      
            return successor
