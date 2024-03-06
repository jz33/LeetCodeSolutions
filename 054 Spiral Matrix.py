'''
54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowCount = len(matrix)
        colCount = len(matrix[0])
        total = rowCount * colCount        
        result = [None] * total
        
        x, y = 0, 0
        level = 0 # circular layer levels
        directions = [(0,1),(1,0),(0,-1),(-1,0)] # right, down, left, up
        dir = 0
        for i in range(total):
            result[i] = matrix[x][y]

            if dir == 0:
                if y == colCount - level - 1:
                    dir = 1
            elif dir == 1:
                if x == rowCount - level - 1:
                    dir = 2
            elif dir == 2:
                if y == level:
                    dir = 3
            elif dir == 3:
                if x == level + 1:
                    dir = 0
                    level += 1

            x += directions[dir][0]
            y += directions[dir][1]

        return result         
