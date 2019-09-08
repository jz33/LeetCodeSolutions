# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        '''
        Return a new tree
        '''
        n = TreeNode(0)
        if t1 and t2:
            n.val = t1.val + t2.val                    
            n.left = self.mergeTrees(t1.left, t2.left)
            n.right = self.mergeTrees(t1.right, t2.right)
        elif t1:
            n.val = t1.val
            n.left = self.mergeTrees(t1.left, None)
            n.right = self.mergeTrees(t1.right, None)
        elif t2:
            n.val = t2.val
            n.left = self.mergeTrees(None, t2.left)
            n.right = self.mergeTrees(None, t2.right)
        else:
            return None

        return n
