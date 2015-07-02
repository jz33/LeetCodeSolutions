import itertools
'''
Unique Binary Search Trees II
https://leetcode.com/problems/unique-binary-search-trees-ii/
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def dfs(nodes):
    trees = []
    for i in range(len(nodes)):
        branches = itertools.product(dfs(nodes[:i]), dfs(nodes[i+1:]))
        for b in branches:
            root = TreeNode(nodes[i])
            root.left, root.right = b[0], b[1]
            trees.append(root)
    return trees or [None]
    
def generateTrees(n):
    return dfs([i+1 for i in range(n)])
    
# UNTESTED
