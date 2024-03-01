'''
240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Example 1:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= n, m <= 300
    -109 <= matrix[i][j] <= 109
    All the integers in each row are sorted in ascending order.
    All the integers in each column are sorted in ascending order.
    -109 <= target <= 109
'''
class Solution:
    '''
    Time Complexity O(max(m,n).
    Different to 74. Search a 2D Matrix
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowCount = len(matrix)
        colCount = len(matrix[0])
        
        # Start from top right
        r, c = 0, colCount - 1
        while r < rowCount and c > -1:
            val = matrix[r][c]
            if val == target:
                return True
            
            if val < target:
                r += 1
            else:
                c -= 1
        
        return False
