'''
590. N-ary Tree Postorder Traversal
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        res = []
        while stack:
            p = stack.pop()
            res.append(p.val)
            
            if p.children:
                for child in p.children:
                    stack.append(child)
        
        return res[::-1]
