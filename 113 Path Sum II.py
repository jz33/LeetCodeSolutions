'''
113 Path Sum II
https://leetcode.com/problems/path-sum-ii/

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
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
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        # Solution based on post-order traversal
        pool = []
        stack = [[[root], root.val]] # [(path from root, sum]
        while stack:
            path, s = stack.pop()
            n = path[-1] # last node
            if self.isLeaf(n):
                if s == sum:
                    pool.append([p.val for p in path])
            else:
                if n.left:
                    stack.append([path + [n.left], s + n.left.val])
                if n.right:
                    stack.append([path + [n.right], s + n.right.val])
            
        return pool
