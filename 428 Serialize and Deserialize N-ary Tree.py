'''
428. Serialize and Deserialize N-ary Tree
https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree

as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not necessarily need to follow this format.

Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated by the null value.

For example, the above tree may be serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

You do not necessarily need to follow the above-suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.

Example 1:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

Example 2:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]

Example 3:

Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    0 <= Node.val <= 104
    The height of the n-ary tree is less than or equal to 1000
    Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    '''
    A level order idea
    '''
    def serialize(self, root: 'Node') -> str:
        if not root:
            return ''
        
        # Do level order serialization
        # Use None as delimiter of nodes
        arr = [root]
        i = 0 # iterator of arr
        while i < len(arr):
            node = arr[i]
            i += 1
            if node is not None:
                arr += node.children
                arr.append(None) # 'None' denotes the end of children
            
        return ','.join(str(n.val) if n is not None else 'N' for n in arr)  
        
    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        
        src = data.split(',')
        si = 1 # iterator of src
        root = Node(src[0])
        queue = [root]
        qi = 0 # iterator of queue
        while si < len(src):
            node = queue[qi]
            qi += 1
            while src[si] != 'N':
                child = Node(src[si])
                node.children.append(child)
                queue.append(child)
                si += 1
            si += 1 # skip 'N'
        return root
    
class Codec2:
    '''
    Real interview questions from Facebook: https://www.1point3acres.com/bbs/thread-1037646-1-1.html
    Use preorder traversal, serialize to like: root{child_1,child_2{child_2_a,child_2_b},child_3}
    '''
    def serialize(self, root: 'Node') -> str:
        if not root:
            return ''
        
        def preorder(node: 'Node') -> str:
            serialized = str(node.val)
            if node.children:
                childrenStrs = []
                for child in node.children:
                    childrenStrs.append(preorder(child))
                serialized = serialized + '{' + ','.join(childrenStrs) + '}'
            return serialized
        
        return preorder(root)
    
    def deserialize(self, data: str) -> 'Node':
        '''
        Example:
        1{3{5,6},2,4}
        1{2,3{6,7{11{14}}},4{8{12}},5{9{13},10}}
        '''
        num = None # Not 0; None means no num there
        root = None
        stack = [] # [nodes]
        for c in data:
            if c == ',':
                # Only create node if there is a num, like "5,";
                # Other case like "},", num should be None, should skip ',' 
                if num is not None:
                    node = Node(num)
                    num = 0
                    stack[-1].children.append(node)
            elif c == '{':
                node = Node(num)
                num = None
                if not stack:
                    root = node
                else:
                    # Link to parent
                    stack[-1].children.append(node)
                stack.append(node)
            elif c == '}':
                # Only create node if there is a num, like "5}",
                # Other case like "}}", should not create Node but only pop
                if num is not None:
                    node = Node(num)
                    num = None
                    stack[-1].children.append(node)
                stack.pop()
            else: # c.isdigit():
                num = int(c) if num is None else num * 10 + int(c)

        if not root and num is not None:
            # single number
            return Node(num)

        return root

        

