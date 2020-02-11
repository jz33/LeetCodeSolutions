'''
1314. Matrix Block Sum
https://leetcode.com/problems/matrix-block-sum/

Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is
the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K,
and (r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
'''
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:        
        rowCount = len(mat)
        colCount = len(mat[0])
        
        # Build prefix matrix
        prefix = [[0] * (colCount+1) for _ in range(rowCount+1)]
        for i in range(rowCount):
            for j in range(colCount):
                prefix[i+1][j+1] = mat[i][j] + prefix[i+1][j] + prefix[i][j+1] - prefix[i][j]
        
        res = [[0] * colCount for _ in range(rowCount)]
        
        for i in range(rowCount):
            for j in range(colCount):
                # Top left point
                tx = max(0, i - K) 
                ty = max(0, j - K)
                
                # Bottom right point
                bx = min(rowCount - 1, i + K)
                by = min(colCount - 1, j + K)
                
                res[i][j] = prefix[bx+1][by+1] - prefix[bx+1][ty] - prefix[tx][by+1] + prefix[tx][ty]
       
        return res
