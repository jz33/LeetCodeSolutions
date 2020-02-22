'''
549. Binary Tree Longest Consecutive Sequence II
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are
both considered valid, but the path [1,2,4,3] is not valid. On the other hand,
the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

Note: All the values of tree nodes are in the range of [-1e7, 1e7].
'''
from typing import Tuple

class Solution:
    def getCount(self, node: TreeNode, leftChildCount: int, rightChildCount: int, isIncrease):
        '''
        @return: either increasing or decreasing sequence count, including node itself
        '''
        counts = [1,1]
        if leftChildCount > 0:
            if isIncrease and node.val == node.left.val + 1 or not isIncrease and node.val == node.left.val - 1:
                counts[0] += leftChildCount
        if rightChildCount > 0:
            if isIncrease and node.val == node.right.val + 1 or not isIncrease and node.val == node.right.val - 1:
                counts[1] += rightChildCount
        return counts
            
    def postorder(self, node: TreeNode) -> Tuple[int, int]:
        '''
        @return: Consecutive sequence count.
        If node is null, return [0,0]
        If node is leaf, return [1,1]
        Otherwise, return [a,b], a is increasing consecutive count,
        b is decreasing consecutive count
        '''
        if not node:
            return 0,0
        
        leftInc, leftDec = self.postorder(node.left)
        rightInc, rightDec = self.postorder(node.right)
              
        # Get single side count, left or right, increasing or decreasing
        incCounts = self.getCount(node, leftInc, rightInc, True)
        decCounts = self.getCount(node, leftDec, rightDec, False)
        
        # Count of both sides must be equal or bigger than single side
        bothCounts = max(incCounts[0] + decCounts[1] - 1, incCounts[1] + decCounts[0] - 1)
        self.maxCount = max(self.maxCount, bothCounts)
        
        return max(incCounts), max(decCounts)
        
    def longestConsecutive(self, root: TreeNode) -> int:
        self.maxCount = 0
        self.postorder(root)
        return self.maxCount
