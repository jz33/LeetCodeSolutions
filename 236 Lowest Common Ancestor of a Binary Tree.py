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
 
Constraints:
    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the tree.
'''
class Solution:
    '''
    Postorder recursive method.
    As p & q will exist, this should be simpler than 1644. Lowest Common Ancestor of a Binary Tree II
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def postorder(node: Union['TreeNode', None]) -> Union['TreeNode', None]:
            '''
            @return: p or q or lca, or None if no p or q not found under this tree
            '''
            if node is None:
                return None
          
            if node.val in [p.val, q.val]:
                # No need to go to children as p, q will exist
                return node

            left = postorder(node.left)
            right = postorder(node.right)
            if left and right:
                return node
            return left or right
        return postorder(root)
