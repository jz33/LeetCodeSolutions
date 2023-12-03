'''
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 
Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        nodes = [root]
        leftToRight = True # Add children from left to right or right to left
        while nodes:
            values = []
            nextNodes = []
            for node in reversed(nodes):
                values.append(node.val)

                if leftToRight:
                    if node.left:
                        nextNodes.append(node.left)
                    if node.right:
                        nextNodes.append(node.right)
                else:
                    if node.right:
                        nextNodes.append(node.right)
                    if node.left:
                        nextNodes.append(node.left)
            
            leftToRight = not leftToRight
            nodes = nextNodes
            result.append(values)
        
        return result
