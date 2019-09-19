'''
106. Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildRecursively(self, postorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        postorder: an subarray of original postorder array
        inorder: an subarray of original inorder array
        '''
        if not postorder or not inorder:
            return None

        v = postorder[-1]                  
        vi = inorder.index(v)  
        
        n = TreeNode(v)  
        n.left = self.buildRecursively(postorder[:vi], inorder[:vi])
        n.right = self.buildRecursively(postorder[vi:-1], inorder[vi+1:])
        
        return n
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.buildRecursively(postorder, inorder)
