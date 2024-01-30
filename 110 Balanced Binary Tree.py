'''
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is
height-balanced

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -104 <= Node.val <= 104
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Standard maximum depth approach based 104. Maximum Depth of Binary Tree
    '''
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def postorder(node: Optional[TreeNode]) -> int:
            nonlocal isBalanced
            if not node or not isBalanced:
                return 0
            leftDepth = postorder(node.left)
            rightDepth = postorder(node.right)
            if abs(leftDepth - rightDepth) > 1:
                isBalanced = False
            return max(leftDepth, rightDepth) + 1

        postorder(root)
        return isBalanced