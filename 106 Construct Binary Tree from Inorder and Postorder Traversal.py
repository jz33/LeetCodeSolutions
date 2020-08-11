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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        size = len(inorder)
        
        # Create a {value : index} map from inorder array
        valueToIndex = dict(zip(inorder, range(size)))
        
        def topDown(left: int, right: int, start: int) -> TreeNode:
            '''
            @left: left index of postorder subarray inclusive
            @right: right index of postorder subarray, inclusive
            @start: left index of inorder subarray, inclusive
            '''
            if left > right:
                return None
            
            # Find the value in inorder array, 
            # compute cut width
            value = postorder[right]
            mid = valueToIndex[value] 
            width = mid - start
            
            node = TreeNode(value)
            node.left = topDown(left, left + width - 1, start)
            node.right = topDown(left + width, right - 1, mid + 1)
            return node
        
        return topDown(0, size - 1, 0)
