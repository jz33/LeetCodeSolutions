"""
510. Inorder Successor in BST II

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node.

# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution:
    def inorderSuccessor(self, p: 'Node') -> 'Node':
        # The successor of p is either its right node's leftmost node
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        else:
        # Or the closest parent that is bigger than p
            while p.parent:
                if p.parent.val > p.val:
                    return p.parent
                p = p.parent                
            else:              
                return None
