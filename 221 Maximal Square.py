'''
221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rowCount = len(matrix)
        if rowCount == 0:
            return 0
        colCount = len(matrix[0])
        if colCount == 0:
            return 0
        
        # dp[i][j] records the largest square ends in i, j
        dp = [[0] * colCount for _ in range(rowCount)]
        
        maxLen = 0
        for i in range(rowCount):
            for j in range(colCount):
                if matrix[i][j] == '1':
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    else:
                        dp[i][j] = 1
                    maxLen = max(maxLen, dp[i][j])
        
        return maxLen * maxLen
