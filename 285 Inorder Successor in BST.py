# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root == None or p == None: return None
        next = None
        if p.right != None:
            next = p.right
            while next.left != None:
                next = next.left
        else:
            while root.val != p.val:
                if root.val > p.val:
                    next = root
                    root = root.left
                elif root.val < p.val:
                    root = root.right
        return next
