'''
1026. Maximum Difference Between Node and Ancestor
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B
where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

Example 1:

Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorder(self, node: TreeNode, maxVal: int, minVal: int):
        if not node:
            return
        
        diff = max(abs(maxVal - node.val), abs(minVal - node.val))
        self.maxDiff = max(self.maxDiff, diff)
        
        self.preorder(node.left, max(maxVal, node.val), min(minVal, node.val))
        self.preorder(node.right, max(maxVal, node.val), min(minVal, node.val))
        
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.maxDiff = 0
        self.preorder(root.left, root.val, root.val)
        self.preorder(root.right, root.val, root.val)
        return self.maxDiff
