'''
449. Serialize and Deserialize BST
https://leetcode.com/problems/serialize-and-deserialize-bst/

Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer, or transmitted across a network connection link to
be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary search tree can be serialized to a string and this string can be
deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    Use 1008 Construct Binary Search Tree from Preorder Traversal
    '''
    def serialize(self, root: TreeNode) -> str:
        p = root
        stack = []
        ls = []
        while p or stack:
            if p:
                ls.append(p.val)
                stack.append(p)
                p = p.left
            else:
                p = stack.pop().right
        res = ' '.join(str(v) for v in ls)
        return res
        
    def deserialize(self, data: str) -> TreeNode:
        if not data or len(data) == 0:
            return None
                
        arr = [int(n) for n in data.split(' ')]
        
        root = TreeNode(arr[0])
        stack = [root]
        for i in range(1, len(arr)):
            e = arr[i]
            n = TreeNode(e)
            
            # stack cannot be empty
            if e < stack[-1].val:
                stack[-1].left = n
            else:
                poped = stack.pop()
                while stack and e > stack[-1].val:
                    poped = stack.pop()
                poped.right = n

            stack.append(n)   
        return root
