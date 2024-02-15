'''
543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -100 <= Node.val <= 100
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Easier than 124. Binary Tree Maximum Path Sum
    '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxNodeCount = 0
        def postorder(node: Optional[TreeNode]) -> int:
            nonlocal maxNodeCount
            if not node:
                return 0
            leftDepth = postorder(node.left)
            rightDepth = postorder(node.right)
            maxNodeCount = max(maxNodeCount, leftDepth + rightDepth + 1)
            return max(leftDepth, rightDepth) + 1
        postorder(root)
        return maxNodeCount - 1

'''
Facebook interview question: find max distance between 2 leaves
https://www.1point3acres.com/bbs/thread-1044702-1-1.html
'''
def maxLeafDistance(root: Optional[TreeNode]) -> Optional[int]:
    maxNodeCount = None

    def postorder(node: Optional[TreeNode]) -> int:
        nonlocal maxNodeCount
        if not node:
            return 0
        leftDepth = postorder(node.left)
        rightDepth = postorder(node.right)

        # The difference to 543: the there could be no leaf on left or right
        # So the question might not have an answer
        if leftDepth > 0 and rightDepth > 0:
            nodeCount = leftDepth + rightDepth + 1
            maxNodeCount = max(maxNodeCount, nodeCount) if maxNodeCount is not None else nodeCount
        return max(leftDepth, rightDepth) + 1
    
    postorder(root)
    return maxNodeCount - 1 if maxNodeCount is not None else None