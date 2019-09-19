'''
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
Accepted
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildRecursively(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        preorder: an subarray of original preorder array
        inorder: an subarray of original inorder array
        '''
        if not preorder or not inorder:
            return None
        
        v = preorder[0]                  
        vi = inorder.index(v)  
        
        n = TreeNode(v)  
        n.left = self.buildRecursively(preorder[1: 1+vi], inorder[:vi])
        n.right = self.buildRecursively(preorder[1+vi:], inorder[vi+1:])
        
        return n
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.buildRecursively(preorder, inorder)
