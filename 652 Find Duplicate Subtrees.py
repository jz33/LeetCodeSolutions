'''
652. Find Duplicate Subtrees
https://leetcode.com/problems/find-duplicate-subtrees/

Given a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        pool = []
        visited = Counter() # {tree serialized string : count}

        def postorder(node: TreeNode) -> str:
            if not node:
                return 'N'
            
            serialized = str(node.val) + ',' + postorder(node.left) + ',' + postorder(node.right)
            
            count = visited[serialized]
            if count == 1:
                pool.append(node)
            visited[serialized] += 1
            
            return serialized       

        postorder(root)
        return pool
