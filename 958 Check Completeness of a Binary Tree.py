'''
958. Check Completeness of a Binary Tree
https://leetcode.com/problems/check-completeness-of-a-binary-tree

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}),
and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:

Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Constraints:
    The number of nodes in the tree is in the range [1, 100].
    1 <= Node.val <= 1000
'''

def getTotalNodeCount(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + getTotalNodeCount(root.left) + getTotalNodeCount(root.right)

class Solution:
    '''
    Different to 110. Balanced Binary Tree,
    as right branch cannot be higher than left branch.
    '''
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        totalNodeCount = getTotalNodeCount(root)

        def preorder(node: Optional[TreeNode], index: int) -> bool:
            if not node:
                return True
            if index >= totalNodeCount:
                return False
            # Recursively compute index of children, if index is out of bound, non-complete
            return preorder(node.left, 2 * index + 1) and preorder(node.right, 2 * (index + 1))

        return preorder(root, 0)
