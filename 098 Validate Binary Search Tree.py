'''
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        Use inorder traversal
        '''
        prev, curr = None, root
        stack = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if prev and prev.val >= curr.val:
                    return False
                prev, curr = curr, curr.right        
        return True
       

class Solution:
    '''
    Preorder
    '''
    def preorder(self, node: TreeNode, minVal: int, maxVal: int) -> bool:
        if not node:
            return True
        
        if node.val <= minVal or node.val >= maxVal:
            return False
        
        return self.preorder(node.left, minVal, node.val) and self.preorder(node.right, node.val, maxVal)
        
    def isValidBST(self, root: TreeNode) -> bool:
        return self.preorder(root, float('-inf'), float('inf'))
     

from typing import Tuple
MAX_INT = float('inf')
MIN_INT = float('-inf')

class Solution:
    def postorder(self, node: TreeNode) -> Tuple[bool, int, int]:
        '''
        @return: is BST, min val, max val
        '''
        if not node:
            return True, MAX_INT, MIN_INT # Notice the order of last 2!
        
        isBSTLeft, minLeft, maxLeft = self.postorder(node.left)
        if not isBSTLeft:
            return False, None, None
        
        isBSTRight, minRight, maxRight = self.postorder(node.right)
        if not isBSTRight:
            return False, None, None
        
        return maxLeft < node.val < minRight, \
               minLeft if node.left else node.val, \
               maxRight if node.right else node.val
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.postorder(root)[0]
