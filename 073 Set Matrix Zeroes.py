'''
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1

Follow up:
    A straightforward solution using O(mn) space is probably a bad idea.
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
        firstColumnHasZero = any(mat[r][0] == 0 for r in range(rowCount))
        firstRowHasZero = any(mat[0][c] == 0 for c in range(colCount))

        # Check zeros inside, if zero, remember onto 1st column and 1st row
        for r in range(rowCount):
            for c in range(colCount):
                if mat[r][c] == 0:
                    mat[r][0] = 0
                    mat[0][c] = 0

        # Mark zeros horizontally according to 1st column
        for r in range(1, rowCount):
            if mat[r][0] == 0:
                for c in range(1, colCount):
                    mat[r][c] = 0

        # Mark zeros vertically according to 1st row
        for c in range(1, colCount):
            if mat[0][c] == 0:
                for r in range(1, rowCount):
                    mat[r][c] = 0
                    
        # Go back to 1st column
        if firstColumnHasZero:
            for r in range(rowCount):
                mat[r][0] = 0

        # Go back to 1st row
        if firstRowHasZero:
            for c in range(colCount):
                mat[0][c] = 0
