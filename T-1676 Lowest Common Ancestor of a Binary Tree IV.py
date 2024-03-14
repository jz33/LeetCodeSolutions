'''
1676. Lowest Common Ancestor of a Binary Tree IV
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

Given the root of a binary tree and an array of TreeNode objects nodes,
return the lowest common ancestor (LCA) of all the nodes in nodes.
All the nodes will exist in the tree, and all values of the tree's nodes are unique.

Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
Output: 2
Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
Output: 1
Explanation: The lowest common ancestor of a single node is the node itself.

Example 3:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
Output: 5
Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -109 <= Node.val <= 109
    All Node.val are unique.
    All nodes[i] will exist in the tree.
    All nodes[i] are distinct.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    This is guarantee that all node in nodes exist in the tree,
    same assumption like 236. Lowest Common Ancestor of a Binary Tree
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def postorder(node):
            if not node:
                return None
            if node in nodes:
                # No need to go to children as nodes are guaranteed to exist
                return node
            left = postorder(node.left)
            right = postorder(node.right)
            if left and right:
                return node
            return left or right
        return postorder(root)