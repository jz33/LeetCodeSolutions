'''
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

 
Follow up: Could you solve it both recursively and iteratively?
'''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        Similar approach to 100. Same Tree
        '''
        if not root:
            return True

        def preorder(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return preorder(p.left, q.right) and preorder(p.right, q.left)

        return preorder(root.left, root.right)
