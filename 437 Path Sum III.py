'''
437. Path Sum III
https://leetcode.com/problems/path-sum-iii/

Given the root of a binary tree and an integer targetSum,
return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards
(i.e., traveling only from parent nodes to child nodes).

Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
    The number of nodes in the tree is in the range [0, 1000].
    -109 <= Node.val <= 109
    -1000 <= targetSum <= 1000
'''
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0

        def preorder(node: Optional[TreeNode], sofar: int, rootSums: 'Counter'):
            nonlocal result, targetSum
            if not node:
                return
            sofar += node.val
            if sofar == targetSum:
                result += 1
            
            result += rootSums[sofar - targetSum]
            
            rootSums[sofar] += 1
            preorder(node.left, sofar, rootSums)
            preorder(node.right, sofar, rootSums)
            rootSums[sofar] -= 1

        rootSums = collections.Counter() # {sum from root to a node : count}
        preorder(root, 0, rootSums)
        return result
