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
        # The successor of p is either its right node's leftmost node
        if p.right:
            t = p.right
            while t.left:
                t = t.left
            return t
        # Or its parent or grand-parent
        else:
            # Find p from root
            t = root
            successor = None
            while t.val != p.val:
                if t.val > p.val:
                    successor = t
                    t = t.left
                else:
                    t = t.right      
            return successor
