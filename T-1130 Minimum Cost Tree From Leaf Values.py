'''
1130. Minimum Cost Tree From Leaf Values
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
(Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.
It is guaranteed this sum fits into a 32-bit integer.

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
 

Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).
'''
from functools import lru_cache
from typing import Tuple

class Solution:
    @lru_cache(None)
    def topDown(self, src: Tuple[int]) -> Tuple[int, int]:
        '''
        @src: input tuple, size > 0
        @return: total, max leaf value
        '''
        size = len(src)
        if size == 1:
            return 0, src[0]
        if size == 2:
            return src[0] * src[1], max(src[0], src[1])
        
        retTotal = float('inf')
        for i in range(1, len(src)):
            leftTotal, leftMax = self.topDown(src[:i])
            rightTotal, rightMax = self.topDown(src[i:])
            retTotal = min(retTotal, leftTotal + rightTotal + leftMax * rightMax)
        return retTotal, max(src)
        
    def mctFromLeafValues(self, arr: List[int]) -> int:
        total, _ = self.topDown(tuple(arr))
        return total
