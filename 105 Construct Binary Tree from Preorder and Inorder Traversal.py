'''
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        size = len(inorder)
        
        # Create a {value : index} map from inorder array for quick lookup
        # The 2 lists must contain unique values, otherwise there can be more than 1 way to build
        valueToIndex = dict([(v, i) for i, v in enumerate(inorder)])
        
        def topDown(left: int, right: int, inorderStart: int) -> Optional[TreeNode]:
            if left == right:
                return TreeNode(preorder[left])
            
            if left > right:
                return None
            
            # Find the value in inorder array, compute cut width
            value = preorder[left]
            inorderIndex = valueToIndex[value] 
            cut = inorderIndex - inorderStart
            
            node = TreeNode(value)
            node.left = topDown(left + 1, left + cut, inorderStart)
            node.right = topDown(left + cut + 1, right, inorderIndex + 1)
            return node
        
        return topDown(0, size - 1, 0)
