'''
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Lever Order Traversal
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        
        # Even though only the right-most node's value on each level is needed,
        # it is necessary to save all nodes as it cannot guarantee right-most node
        # is always from the right-most parent.
        # This is different to 545. Boundary of Binary Tree
        row = [root]
        while row:
            newRow = []
            for i, node in enumerate(row):
                if i == len(row) - 1:
                    result.append(node.val)
                if node.left:
                    newRow.append(node.left)
                if node.right:
                    newRow.append(node.right)
            row = newRow
        return result

class Solution:
    '''
    Preorder traversal, use less space
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        
        def preorder(node: TreeNode, level: int):
            nonlocal result
            if level == len(result):
                result.append(node.val)

            # The trick is: always push the right node first,
            # then it is guaranteed that the node is the right-most when reach a new level
            if node.right:
                preorder(node.right, level + 1)
            if node.left:
                preorder(node.left, level + 1)
        
        preorder(root, 0)
        return result
            