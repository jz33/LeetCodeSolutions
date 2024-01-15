'''
687. Longest Univalue Path
https://leetcode.com/problems/longest-univalue-path/

Given the root of a binary tree, return the length of the longest path,
where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

Example 1:

Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).

Example 2:

Input: root = [1,4,5,4,4,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 4).

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -1000 <= Node.val <= 1000
    The depth of the tree will not exceed 1000.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        maxNodeCount = 1

        def postorder(node: Optional[TreeNode]) -> Tuple[int, int]:
            '''
            @return: (value, node count)
            '''
            nonlocal maxNodeCount
            if not node:
                return (None, 0)
            
            leftVal, leftCount = postorder(node.left)
            rightVal, rightCount = postorder(node.right)

            totalCount = 1 # total count of nodes of left and right path
            singlePathCount = 1 # max count of nodes of left or right path
            if node.val == leftVal:
                totalCount += leftCount
                singlePathCount = max(singlePathCount, 1 + leftCount)
            if node.val == rightVal:
                totalCount += rightCount
                singlePathCount = max(singlePathCount, 1 + rightCount)

            # Unlike 124, here, totalCount should always >= singlePathCount
            maxNodeCount = max(maxNodeCount, totalCount)
            return node.val, singlePathCount
        
        postorder(root)
        return maxNodeCount - 1