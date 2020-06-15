'''
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''
class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not mat or not mat[0]:
            return
        
        rowCount = len(mat)
        colCount = len(mat[0])
        
        # Check if 1st column and 1st row will be all zero
        firstColumnIsZero = any(mat[i][0] == 0 for i in range(rowCount))
        firstRowIsZero = any(mat[0][i] == 0 for i in range(colCount))

        # Check zeros inside, if zero, remember onto 1st column and 1st row
        for i in range(rowCount):
            for j in range(colCount):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0

        # Mark zeros horizontally according to 1st column
        for i in range(1, rowCount):
            if mat[i][0] == 0:
                for j in range(1, colCount):
                    mat[i][j] = 0

        # Mark zeros vertically according to 1st row
        for j in range(1, colCount):
            if mat[0][j] == 0:
                for i in range(1, rowCount):
                    mat[i][j] = 0
                    
        # Go back to 1st column
        if firstColumnIsZero:
            for i in range(rowCount):
                mat[i][0] = 0

        # Go back to 1st row
        if firstRowIsZero:
            for j in range(colCount):
                mat[0][j] = 0
