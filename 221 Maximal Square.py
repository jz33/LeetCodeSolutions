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
        if not matrix or not matrix[0]:
            return 0
        
        rowCount = len(matrix)
        colCount = len(matrix[0])
        
        # dp[i][j] keeps the size of maximal square on (i,j)
        dp = [[0] * colCount for _ in range(rowCount)]
        for i in range(rowCount):
            for j in range(colCount):
                if matrix[i][j] == '1':
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    else:
                        dp[i][j] = 1
        
        maxSize = max(dp[i][j] for i in range(rowCount) for j in range(colCount))
        return maxSize * maxSize
