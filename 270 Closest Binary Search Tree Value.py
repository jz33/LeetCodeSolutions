'''
270. Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value/

Given the root of a binary search tree and a target value,
return the value in the BST that is closest to the target.
If there are multiple answers, print the smallest.

Example 1:

Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:

Input: root = [1], target = 4.428571
Output: 1

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    0 <= Node.val <= 109
    -109 <= target <= 109
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        curr = root
        lowerBound = float('-inf')
        upperBound = float('inf')
        while curr:
            if target == curr.val:
                return curr.val
            if target < curr.val:
                upperBound = curr.val
                curr = curr.left
            else:
                lowerBound = curr.val
                curr = curr.right
        return lowerBound if target - lowerBound <= upperBound - target else upperBound