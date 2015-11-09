'''
Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialize and Deserialize tree by level order traversal
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.  
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        # Cannot use i in xrange(len(queue))
        i = 0
        while i < len(queue):
            n = queue[i]
            if n is not None:   
                queue.append(n.left)
                queue.append(n.right)
            i += 1

        i = len(queue) - 1
        while i > -1:
            if queue[i] != None: break
            i -= 1
        queue = queue[:i+1]
 
        for i,v in enumerate(queue):
            if v is not None:
                queue[i] = str(v.val)
        return queue

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0: return None
        root = TreeNode(data[0])
        queue = [root]
        i = 1
        j = 0
        while i < len(data):
            n = queue[j]
            j += 1
            v = data[i]
            i += 1
            if v is not None:
                n.left = TreeNode(v)
                queue.append(n.left)
            if i == len(data): break
            v = data[i]
            i += 1
            if v is not None:
                n.right = TreeNode(v)
                queue.append(n.right)
        return root

sol = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

r = sol.serialize(root)
print r
t = sol.deserialize(r)
print t, t.left, t.right,t.left.left,t.left.right,t.right.left,t.right.right
