'''
1644. Lowest Common Ancestor of a Binary Tree II
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii

Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q.
If either node p or q does not exist in the tree, return null.
All values of the nodes in the tree are unique.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.

Example 3:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    '''
    The p, q may not exist in tree. So this is different to
    236. Lowest Common Ancestor of a Binary Tree
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        foundP, foundQ = False, False

        def postorder(node: Union['TreeNode', None]) -> Union['TreeNode', None]:
            '''
            @return: p or q or lca, or None if no p or q not found under this tree
            '''
            nonlocal foundP, foundQ
            if foundP and foundQ:
                return None
            if node is None:
                return None

            left = postorder(node.left)
            right = postorder(node.right)
            if left and right:
                # This node is the LCA, as p and q are on each branch
                return node
            elif node.val == p.val:
                # This node is p, it could be the LCA.
                foundP = True
                return node
            elif node.val == q.val:
                # This node is q, it could be the LCA.
                foundQ = True
                return node
            elif left:
                # Found p or q in left branch
                return left
            elif right:
                # Found p or q in left branch
                return right
            else:
                # Not found p or q in this tree
                return None

        lca = postorder(root)
        # Even if lca is not None, it is possible only one of p or q exists,
        # therefore must make sure both p and q are found
        return lca if foundP and foundQ else None
