'''
240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
    
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Same method to 74. Search a 2D Matrix
        '''
        if not matrix or not matrix[0]:
            return False
        
        rowCount = len(matrix)
        colCount = len(matrix[0])
        
        # Start from top right
        x, y = 0, colCount - 1
        while x < rowCount and y > -1:
            val = matrix[x][y]
            if val == target:
                return True
            
            if val < target:
                x += 1
            else:
                y -= 1
        
        return False
