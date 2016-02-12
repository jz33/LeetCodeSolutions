from sys import maxint
'''
Largest BST Subtree
https://leetcode.com/problems/largest-bst-subtree/
'''
def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
    
maxCtr = 1
minint = -maxint - 1

def rec(node):
    '''
    return: is BST, node count, min val, max val
    '''
    global maxCtr
    if node is None:
        return True,0,maxint,minint
    if node.left is None and node.right is None:
        return True,1,node.val,node.val
        
    lt_isBST, lt_ctr, lt_min, lt_max = rec(node.left)   
    rt_isBST, rt_ctr, rt_min, rt_max = rec(node.right)
    
    if lt_isBST and rt_isBST:
        if lt_max < node.val and node.val < rt_min:
            r_ctr = lt_ctr+rt_ctr+1
            r_min = lt_min if node.left is not None else node.val
            r_max = rt_max if node.right is not None else node.val
            maxCtr = max(maxCtr,r_ctr)
            return True, r_ctr, r_min, r_max
    
    return False,0,0,0
    
def largestBSTSubtree(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    global maxCtr
    if root is None: return 0
    maxCtr = 1
    rec(root)
    return maxCtr
