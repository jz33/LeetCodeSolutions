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

class Solution:
    def postorder(self, node: TreeNode) -> str:
        if not node:
            return 'N'
        
        serilized = str(node.val) + ',' + self.postorder(node.left) + ',' + self.postorder(node.right)
        
        ctr = self.visited[serilized]
        if ctr == 1:
            self.pool.append(node)
        self.visited[serilized] += 1
        
        return serilized
        
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.pool = []
        self.visited = collections.Counter() # {tree serilized string : count}
        self.postorder(root)
        return self.pool
