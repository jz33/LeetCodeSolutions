'''
542. 01 Matrix
https://leetcode.com/problems/01-matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 104
    1 <= m * n <= 104
    mat[i][j] is either 0 or 1.
    There is at least one 0 in mat
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rowCount = len(mat)
        colCount = len(mat[0])
        inf = rowCount * colCount
        dp = [[0] * colCount for _ in range(rowCount)]
    
        # From top left to bottom right, update each cell using left and upper cells
        for r in range(rowCount):
            for c in range(colCount):
                if mat[r][c] != 0:
                    dp[r][c] = min(inf, dp[r-1][c]+1 if r > 0 else inf, dp[r][c-1]+1 if c > 0 else inf)

        # From bottom right to top left, update each cell using right and bottom cells
        for r in range(rowCount-1,-1,-1):
            for c in range(colCount-1,-1,-1):
                if mat[r][c] != 0:
                    dp[r][c] = min(dp[r][c], dp[r+1][c]+1 if r+1 < rowCount else inf, dp[r][c+1]+1 if c+1 <colCount else inf)

        return dp

        