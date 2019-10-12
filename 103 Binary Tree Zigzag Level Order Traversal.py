'''
103 Binary Tree Zigzag Level Order Traversal
https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        isOddRow = True
        stack = [root]    
        
        while stack:
            outputRow = []
            nextStack = []
            while stack:
                n = stack.pop()
                outputRow.append(n.val)
                    
                if isOddRow:
                    # Oddy row nodes will put left child in first  
                    if n.left:
                        nextStack.append(n.left)
                    if n.right:
                        nextStack.append(n.right)
                else:
                    if n.right:
                        nextStack.append(n.right)
                    if n.left:
                        nextStack.append(n.left)
                        
            isOddRow = not isOddRow
            stack = nextStack
            if outputRow:
                ans.append(outputRow)
                
        return ans
