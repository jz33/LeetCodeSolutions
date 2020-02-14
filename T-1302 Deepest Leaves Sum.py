'''
1302. Deepest Leaves Sum
https://leetcode.com/problems/deepest-leaves-sum/

Given a binary tree, return the sum of values of its deepest leaves.
 
Example 1:

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getDepth(self, node: TreeNode) -> int:
        if not node:
            return 0     
        return max(self.getDepth(node.left), self.getDepth(node.right)) + 1
    
    def preorder(self, node: TreeNode, depth: int):
        if node:
            if depth == self.maxDepth:
                self.total += node.val
            else:
                self.preorder(node.left, depth + 1)
                self.preorder(node.right, depth + 1)
            
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.maxDepth = self.getDepth(root)
        self.total = 0
        self.preorder(root, 1)
        return self.total
