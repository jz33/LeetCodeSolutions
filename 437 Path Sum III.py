'''
437. Path Sum III
https://leetcode.com/problems/path-sum-iii/

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, node: TreeNode, total: int, rootSums: 'Counter'):
        '''
        @total: total sum from root till parent
        '''
        if not node:
            return
        
        # If root till current node's sum is target?
        total += node.val
        if total == self.target:
            self.result += 1
        
        # If there is a path from root to a parent node of curr node
        # whose path sum is total - target, that means the child
        # node of this parent node to current node has sum of target.
        self.result += rootSums[total - self.target]
        
        rootSums[total] += 1
        self.preorder(node.left, total, rootSums)
        self.preorder(node.right, total, rootSums)
        rootSums[total] -= 1

    def pathSum(self, root: TreeNode, target: int) -> int:
        self.result = 0 # result
        self.target = target
        
        # rootSums records the sums from root to all previous nodes
        # for this question's example, if at node 1, rootSums should 
        # contain [10, 15, 17]
        rootSums = collections.Counter()
        self.preorder(root, 0, rootSums)
        
        return self.result
