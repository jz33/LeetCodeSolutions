'''
112. Path Sum
https://leetcode.com/problems/path-sum/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that
adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22
'''
          
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isLeaf(self, n: TreeNode) -> bool:
        return (not n.left and not n.right)
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        # [(node, sum from root)]
        stack = [(root, root.val)] 
        while stack:
            n, s = stack.pop()
            if self.isLeaf(n):
                if s == sum:
                    return True
            else:
                if n.left:
                    stack.append((n.left, s + n.left.val))
                if n.right:
                    stack.append((n.right, s + n.right.val))
            
        return False
