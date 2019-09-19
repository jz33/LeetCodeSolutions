'''
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue = deque() # Essentially, only need a queue
        queue.append(root)
        
        while queue:
            size = len(queue)
            row = [None] * size
            for i in range(size):
                n = queue.popleft()
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
                row[i] = n.val
            res.append(row)
        
        return res
