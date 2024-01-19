'''
106. Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree
and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:
    1 <= inorder.length <= 3000
    postorder.length == inorder.length
    -3000 <= inorder[i], postorder[i] <= 3000
    inorder and postorder consist of unique values.
    Each value of postorder also appears in inorder.
    inorder is guaranteed to be the inorder traversal of the tree.
    postorder is guaranteed to be the postorder traversal of the tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        size = len(inorder)
        
        # Create a {value : index} map from inorder array for quick lookup
        # The 2 lists must contain unique values, otherwise there can be more than 1 way to build
        valueToIndex = dict([(v, i) for i, v in enumerate(inorder)])
        
        def topDown(left: int, right: int, inorderStart: int) -> Optional[TreeNode]:
            if left == right:
                return TreeNode(postorder[right])
            
            if left > right:
                return None
            
            # Find the value in inorder array, compute cut width
            value = postorder[right]
            inorderIndex = valueToIndex[value] 
            cut = inorderIndex - inorderStart
            
            node = TreeNode(value)
            node.left = topDown(left, left + cut - 1, inorderStart)
            node.right = topDown(left + cut, right - 1, inorderIndex + 1)
            return node
        
        return topDown(0, size - 1, 0)
