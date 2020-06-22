'''
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
         
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        root.left, root.right = root.right, root.left
        
        # No need to care about returns
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
        Iterative level order traversal
        '''
        if not root:
            return root
        
        stack = [root]
        while stack:
            newStack = []
            for node in stack:
                node.left, node.right = node.right, node.left
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
            stack = newStack
        return root  
