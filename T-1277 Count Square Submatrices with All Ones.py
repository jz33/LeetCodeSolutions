'''
1277. Count Square Submatrices with All Ones
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

Output: 15

Explanation:

There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        '''
        Similar to 221. Maximal Square
        '''
        if not matrix or not matrix[0]:
            return 0
        
        rowCount = len(matrix)
        colCount = len(matrix[0])
        
        # dp[i][j] keeps the size of maximal square on (i,j)
        dp = [[0] * colCount for _ in range(rowCount)]
        for i in range(rowCount):
            for j in range(colCount):
                if matrix[i][j] == 1:
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    else:
                        dp[i][j] = 1
                    
        return sum(dp[i][j] for i in range(rowCount) for j in range(colCount))          
