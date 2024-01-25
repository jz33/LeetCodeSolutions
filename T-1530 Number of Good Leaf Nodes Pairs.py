'''
1530. Number of Good Leaf Nodes Pairs
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

You are given the root of a binary tree and an integer distance.
A pair of two different leaf nodes of a binary tree is said to be good
if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

Example 1:

Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3.
This is the only good pair.

Example 2:

Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2.
The pair [4,6] is not good because the length of their shortest path between them is 4.

Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].

Constraints:
    The number of nodes in the tree is in the range [1, 210].
    1 <= Node.val <= 100
    1 <= distance <= 10
'''
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getTwoArraySumCount(left: List[int], right: List[int], target: int) -> int:
    '''
    Get count of pairs from 2 sorted arrays whose sum is less or equal to target
    '''
    count = 0
    ri = len(right) - 1
    li = 0
    while li < len(left) and ri >= 0:
        if left[li] + right[ri] <= target:
            # All (left[li], right[<=ri]) pairs are valid
            count += ri + 1
            li += 1
        else:
            ri -= 1
    return count

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        result = 0
        def postorder(node: TreeNode) -> List[int]:
            '''
            @return: sorted list of all depth from node to all its leaves
            '''
            nonlocal result
            leafDepths = []
            if node.left and node.right:
                lefts = postorder(node.left)
                rights = postorder(node.right)
                result += getTwoArraySumCount(lefts, rights, distance)
                leafDepths = sorted(lefts + rights)
            elif node.left:
                leafDepths = postorder(node.left)
            elif node.right:
                leafDepths = postorder(node.right)
            else:
                leafDepths = [0]

            return [depth + 1 for depth in leafDepths]

        postorder(root)
        return result
