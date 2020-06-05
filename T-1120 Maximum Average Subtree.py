'''
1120. Maximum Average Subtree
https://leetcode.com/problems/maximum-average-subtree/

Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants.
The average value of a tree is the sum of its values, divided by the number of nodes.)

Example 1:

Input: [5,6,1]
Output: 6.00000
Explanation: 
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Tuple

class Solution:
    def postorder(self, node) -> Tuple[int, int]:
        # return: [node count, total value]
        if not node:
            return 0, 0
        
        leftCount, leftTotal = self.postorder(node.left)
        rightCount, rightTotal = self.postorder(node.right)
        totalCount = leftCount + rightCount + 1
        totalValue = leftTotal + rightTotal + node.val
        
        self.maxAvg = max(self.maxAvg, totalValue / totalCount)   
        return totalCount, totalValue
        
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.maxAvg = 0.0
        self.postorder(root)
        return self.maxAvg
