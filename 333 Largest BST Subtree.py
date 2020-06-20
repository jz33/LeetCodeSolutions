'''
333. Largest BST Subtree
https://leetcode.com/problems/largest-bst-subtree/

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST),
where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Tuple

MAX_INT = float('inf')
MIN_INT = float('-inf')
                
class Solution:
    def postorder(self, node: TreeNode) -> Tuple[bool, int, int, int]:
        '''
        @return: the status of a tree with node as root
        1. Whether this tree is BST
        2. Total node count
        3. The minimum node value
        4. The maximum node value
        '''
        if not node:
            return True, 0, MAX_INT, MIN_INT # Notice the order of last 2!
        
        if node.left is None and node.right is None:
            self.maxTotal = max(self.maxTotal, 1)
            return True, 1, node.val, node.val
        
        isBSTLeft, totalLeft, minLeft, maxLeft = self.postorder(node.left)
        isBSTRight, totalRight, minRight, maxRight = self.postorder(node.right)
    
        isBST = isBSTLeft and isBSTRight and (maxLeft < node.val < minRight)
        if isBST:
            total = totalLeft + totalRight + 1
            if total > 0:
                self.maxTotal = max(self.maxTotal, total)
            return True, total, min(node.val, minLeft, minRight), max(node.val, maxLeft, maxRight)
        else:
            return False, 0, 0, 0
        
    def largestBSTSubtree(self, root: TreeNode) -> int:
        '''
        Same question to 1373 Maximum Sum BST in Binary Tree
        '''
        self.maxTotal = 0
        self.postorder(root)
        return self.maxTotal
