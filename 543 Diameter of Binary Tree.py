'''
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them. 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rec(self, node):
        '''
        Similary to 124 Binary Tree Maximum Path Sum
        Return count of one-side plus one (singleChoice)
        '''
        if not node:
            return 0
        
        leftCount = self.rec(node.left)
        rightCount = self.rec(node.right)
        
        # Max count on 1 node is always the sum of 2 branches
        self.maxCount = max(self.maxCount, leftCount + rightCount + 1)
        
        # Return only 1 side of branch
        return max(leftCount, rightCount) + 1
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxCount = 1
        self.rec(root)
        return self.maxCount - 1
