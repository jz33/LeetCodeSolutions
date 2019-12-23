'''
1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

Given a m x n matrix mat and an integer threshold. Return the maximum side-length of a square with
a sum less than or equal to threshold or return 0 if there is no such square.

Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.

Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0

Example 3:

Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
Output: 3

Example 4:

Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output: 2
'''
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rowCount = len(mat)
        colCount = len(mat[0])
        
        # Build prefix sum matrix
        accu = [[0] * (colCount + 1) for _ in range(rowCount + 1)]
        for i in range(rowCount):
            for j in range(colCount):
                accu[i+1][j+1] = accu[i][j+1] + accu[i+1][j] - accu[i][j] + mat[i][j]
      
        # Binary search
        maxSide = 0
        for i in range(rowCount):
            for j in range(colCount):
                if i == 0 or j == 0:
                    if maxSide == 0 and mat[i][j] <= threshold:
                        maxSide = 1
                else:
                    # The square starts at (i,j)
                    # Try expand to right and top, find fit side length            
                    left = 1 # minimun square side length
                    right = min(i, j) + 1 # maximun square side length
                    while left <= right:
                        mid = left + (right - left) // 2
                        area = accu[i+1][j+1] - accu[i+1-mid][j+1] - accu[i+1][j+1-mid] + accu[i+1-mid][j+1-mid]
                        if area <= threshold:
                            maxSide = max(maxSide, mid)
                            left = mid + 1
                        else:
                            right = mid - 1
        return maxSide
