'''
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/

You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
'''
class Solution:
    '''
    Different 240. Search a 2D Matrix II because 
    The first integer of each row is greater than the last integer of the previous row.
    If expand the matrix to an array, it is sorted.
    Binary search: O(log(m*n))
    Can still use 240 method, but will be slower
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowCount = len(matrix)
        colCount = len(matrix[0])
        left = 0
        right = rowCount * colCount - 1
        while left <= right:
            mid = left + (right - left) // 2
            midRow = mid // colCount
            midCol = mid % colCount
            midVal = matrix[midRow][midCol]
            if midVal == target:
                return True
            elif midVal < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
