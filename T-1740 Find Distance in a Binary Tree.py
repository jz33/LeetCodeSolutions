'''
1740. Find Distance in a Binary Tree
https://leetcode.com/problems/find-distance-in-a-binary-tree/

Given the root of a binary tree and two integers p and q,
return the distance between the nodes of value p and value q in the tree.

The distance between two nodes is the number of edges on the path from one to the other.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
Output: 3
Explanation: There are 3 edges between 5 and 0: 5-3-1-0.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7
Output: 2
Explanation: There are 2 edges between 5 and 7: 5-2-7.

Example 3:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5
Output: 0
Explanation: The distance between a node and itself is 0.

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    0 <= Node.val <= 109
    All Node.val are unique.
    p and q are values in the tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    LCA question
    '''
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0

        findLCA = False # The flag is necessary to avoid count distance from LCA to root
        distance = 0
        def postorder(node: Optional[TreeNode]) -> Optional[TreeNode]:
            nonlocal distance, findLCA
            if findLCA or not node:
                return None
            leftResult = postorder(node.left)
            rightResult = postorder(node.right)
            if findLCA:
                # Notice the LCA can be found in subroutes
                return None
            if leftResult and rightResult:
                # This node is the LCA
                distance += 2
                findLCA = True
            elif leftResult:
                distance += 1
                if node.val in [p, q]:
                    # This node is the LCA
                    findLCA = True
            elif rightResult:
                distance += 1
                if node.val in [p, q]:
                    # This node is the LCA
                    findLCA = True
            # As always in LCA question, either return node, left result, right result, or None
            return node if node.val in [p, q] or leftResult and rightResult else leftResult or rightResult
 
        postorder(root)
        return distance
            