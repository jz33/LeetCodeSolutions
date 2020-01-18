'''
311. Sparse Matrix Multiplication
https://leetcode.com/problems/sparse-matrix-multiplication/

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
'''
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        rowCount = len(A)
        midCount = len(B) # or len(A[0])
        colCount = len(B[0])
        
        res = [[0] * colCount for _ in range(rowCount)]

        for i in range(rowCount):
            for j in range(midCount):
                if A[i][j] != 0: # without this line, this is normal matrix multiplication
                    for k in range(colCount):
                        res[i][k] += A[i][j] * B[j][k]
                        
        return res
