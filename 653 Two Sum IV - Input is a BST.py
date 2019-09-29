'''
653. Two Sum IV - Input is a BST
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST
such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        visited = set()
        # Traverse the tree
        stack = []
        p = root
        while p or stack:
            if p:
                q = k - p.val
                if q in visited:
                    return True
                visited.add(p.val)
                
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                p = p.right
        
        return False
