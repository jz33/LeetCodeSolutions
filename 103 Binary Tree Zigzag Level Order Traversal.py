'''
103 Binary Tree Zigzag Level Order Traversal
https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''
class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        ans = []
        if root is None: return ans
        
        isEven = True
        even = [root]
        oddy = []
        
        while len(even) != 0 or len(oddy) != 0:
            row = []
            if isEven:
                isEven = False
                oddy = []
                for e in reversed(even):
                    row.append(e.val)
                    if e.left  != None: oddy.append(e.left)
                    if e.right != None: oddy.append(e.right)
            else:
                isEven = True
                even = []
                for e in reversed(oddy):
                    row.append(e.val)
                    if e.right != None: even.append(e.right)
                    if e.left  != None: even.append(e.left)                   
            if len(row) != 0: ans.append(row)
        return ans
