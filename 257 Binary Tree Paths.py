from copy import deepcopy
'''
Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/
'''
NEXT = "->"

def rec(root,buf,pool):
    if root is None:
        return
    if root.left is None and root.right is None:
        pool.append(deepcopy(buf) + str(root.val))
    elif root.left is not None and root.right is None:
        rec(root.left, buf + str(root.val) + NEXT, pool)
    elif root.left is None and root.right is not None:
        rec(root.right,buf + str(root.val) + NEXT, pool)
    else:
        newBuf = deepcopy(buf)
        rec(root.left, buf + str(root.val) + NEXT, pool)
        rec(root.right, newBuf + str(root.val) + NEXT, pool)

def binaryTreePaths(root):
    pool = []
    buf = ""
    rec(root,buf,pool)
    return pool
