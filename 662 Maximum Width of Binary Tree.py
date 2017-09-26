class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
'''
662 Maximum Width of Binary Tree
'''
def widthOfBinaryTree(root):
    """
    Level order traversal
    """
    if root == None: return None
    mw = 0
    dq = deque()
    dq.append((root,0))
    while len(dq) > 0:
        p,left = dq.popleft()
        dq.appendleft((p,left))
        p,right = dq.pop()
        dq.append((p,right))
        mw = max(mw, right - left)

        for _ in xrange(len(dq)):
            p,v = dq.popleft()
            if p.left != None:
                dq.append((p.left,(v << 1)))
            if p.right != None:
                dq.append((p.right,(v << 1)+1))
    return mw+1
