'''
589. N-ary Tree Preorder Traversal
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = [] # [(node, index of last visited children)]
        res = []
        p = root
        
        while p or stack:
            if p:
                res.append(p.val)
                
                # Always go leftmost first
                if p.children:
                    stack.append((p, 0))
                    p = p.children[0]                    
                else:
                    # No more children. Go to 'else'
                    p = None
            else:
                p, i = stack.pop()
                
                # Go to sibling
                i += 1
                if p.children and i < len(p.children):
                    stack.append((p, i))
                    p = p.children[i]
                else:
                    # No more children. Go to 'else' again and get parent
                    p = None
                                  
        return res
