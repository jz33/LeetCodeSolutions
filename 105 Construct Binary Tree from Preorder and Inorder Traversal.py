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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        size = len(inorder)
        
        # Create a {value : index} map from inorder array
        valueToIndex = dict(zip(inorder, range(size)))
        
        def topDown(left: int, right: int, start: int) -> TreeNode:
            '''
            @left: left index of preorder subarray inclusive
            @right: right index of preorder subarray, inclusive
            @start: left index of inorder subarray, inclusive
            '''
            if left > right:
                return None
            
            # Find the value in inorder array, 
            # compute cut width
            value = preorder[left]
            mid = valueToIndex[value] 
            width = mid - start
            
            node = TreeNode(value)
            node.left = topDown(left + 1, left + width, start)
            node.right = topDown(left + width + 1, right, mid + 1)
            return node
        
        return topDown(0, size - 1, 0)
