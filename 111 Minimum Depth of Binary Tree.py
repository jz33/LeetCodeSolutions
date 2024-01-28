'''
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
    The number of nodes in the tree is in the range [0, 105].
    -1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    '''
    Different to 104. Maximum Depth of Binary Tree, as a null child cannot count to depth
    '''
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def postorder(node: TreeNode) -> int:
            if not node.left and not node.right:
                return 1
            if not node.left:
                return postorder(node.right) + 1
            if not node.right:
                return postorder(node.left) + 1
            return min(postorder(node.left), postorder(node.right)) + 1

        return postorder(root)