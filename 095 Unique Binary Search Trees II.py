'''
95. Unique Binary Search Trees II
https://leetcode.com/problems/unique-binary-search-trees-ii/

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorder(self, values: List[int]) -> List[TreeNode]:
        trees = []
        for i in range(len(values)):
            lefts = self.postorder(values[:i])
            rights = self.postorder(values[i+1:])
            for left in lefts:
                for right in rights:
                    root = TreeNode(values[i])
                    root.left = left
                    root.right = right
                    trees.append(root)
        return trees if trees else [None]
    
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n < 1:
            return []
        return self.postorder(list(range(1 ,n+1)))
