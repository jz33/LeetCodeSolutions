'''
1289. Minimum Falling Path Sum II
https://leetcode.com/problems/minimum-falling-path-sum-ii/

Given a square grid of integers arr, a falling path with non-zero shifts is a choice of
exactly one element from each row of arr, such that no two elements chosen in adjacent rows are in the same column.

Return the minimum sum of a falling path with non-zero shifts.

Example 1:

Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13

Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.
 

Constraints:

1 <= arr.length == arr[i].length <= 200
-99 <= arr[i][j] <= 99
'''
from typing import Tuple

class Solution:
    def getMins(self, arr: List[int]) -> List[Tuple[int, int]]:
        '''
        Get the 1st & 2nd minimum of array
        '''
        res = [None, None] # res[0] is smallest, res[1] is 2nd smallest
        for i, e in enumerate(arr):
            if res[0] is None:
                res[0] = (i,e)
            elif res[1] is None or e < res[1][1]:
                res[1] = (i,e)
                if res[1][1] < res[0][1]:
                    res[0], res[1] = res[1], res[0]
        return res
        
        
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if not A or not A[0]:
            return 0
        
        width = len(A)
        if width == 1:
            return A[0][0]
        
        dp = [0] * width
        for i in range(width):
            m0, m1 = self.getMins(dp)         
            for j in range(width):
                # Choose minimum from previous row. 
                # If previous minimum is in same column, choose 2nd minimum
                dp[j] = A[i][j] + m0[1] if m0[0] != j else A[i][j] + m1[1]
                
        return min(dp)
