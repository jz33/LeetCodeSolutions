'''
1008. Construct Binary Search Tree from Preorder Traversal
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node,
any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.
Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, len(preorder)):
            e = preorder[i]
            n = TreeNode(e)
            
            # stack cannot be empty
            if e < stack[-1].val:
                stack[-1].left = n
            else:
                poped = stack.pop()
                while stack and e > stack[-1].val:
                    poped = stack.pop()
                poped.right = n

            stack.append(n)
        return root
