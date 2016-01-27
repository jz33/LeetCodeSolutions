'''
Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialize and Deserialize tree by level order traversal
'''
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.  
        :type root: TreeNode
        :rtype: list[object]
        """
        if root is None: return []
        
        queue = [root]
        i = 0 # next node position in queue
        while i < len(queue):
            n = queue[i]
            if n is not None:
                queue.append(n.left)
                queue.append(n.right)
            i += 1
        
        # Remove trailing Nones
        for i in xrange(len(queue)-1,-1,-1):
            if queue[i] != None: 
                break
        
        # Convert object to value
        for i in xrange(len(queue)):
            queue[i] = queue[i].val if queue[i] is not None else None
            
        return queue[:i+1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: list[object]
        :rtype: TreeNode
        """
        if len(data) == 0: return None
        
        root = TreeNode(data[0])
        queue = [root]
        i = 0 # next node position in queue
        j = 1 # next object position in data
        while j < len(data):
            n = queue[i]
            i += 1
            v = data[j]
            j += 1
            if v is not None:
                n.left = TreeNode(v)
                queue.append(n.left)
            if j == len(data): break
            v = data[j]
            j += 1
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
