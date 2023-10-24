'''
236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that
has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
    
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of
itself according to the LCA definition.
 
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isChildExisting(self, root: 'TreeNode' or None, child: 'TreeNode'):
        if not root:
            return False;
        curr = root
        stack = []
        while curr or stack:
            if curr is not None:
                if curr.val == child.val:
                    return True
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop().right
        return False
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode' or None:
        # Find the 1st node. The Find 2nd node from the 1st node or 1st node's parent nodes.
        # The LCA is either 1st node or one of 1st node's parents.
        
        firstNode = None
        secondNode = None

        # Preorder traversal to find 1st node
        curr = root
        stack = []
        while curr or stack:
            if curr is not None:
                if curr.val == p.val:
                    firstNode = p
                    secondNode = q
                    break
                elif curr.val == q.val:
                    firstNode = q
                    secondNode = p
                    break
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop().right

        # Not even found 1st node, no LCA
        if firstNode is None:
            return None

        # The 1st node can be the LCA if 2nd node is found in its children
        if self.isChildExisting(firstNode, secondNode):
            return firstNode

        # The LCA can be a parent of 1st node
        while stack:
            lca = stack.pop()
            # Only need to check the node itself + right branch,
            # as left branch is already traversed
            if lca.val == secondNode.val or self.isChildExisting(lca.right, secondNode):
                return lca
  
        return None
