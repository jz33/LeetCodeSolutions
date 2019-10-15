'''
429. N-ary Tree Level Order Traversal
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        res = []        
        queue = deque()
        queue.append(root)
        while queue:
            row = []
            for _ in range(len(queue)):
                p = queue.popleft()
                row.append(p.val)

                if p.children:
                    for child in p.children:
                        queue.append(child)
              
            res.append(row)
        return res
