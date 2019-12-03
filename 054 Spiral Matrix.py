'''
54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowCount = len(matrix)
        if not rowCount:
            return []
        
        colCount = len(matrix[0])
        if not colCount:
            return []
        
        total = rowCount * colCount        
        res = [None] * total
        
        x, y = 0, 0
        level = 0 # circular layer levels
        directions = [(0,1),(1,0),(0,-1),(-1,0)] # right, down, left, up
        di = 0
        for i in range(total):
            res[i] = matrix[x][y]
            
            if di == 0:
                if y == colCount - level - 1:
                    di = 1
            elif di == 1:
                if x == rowCount - level - 1:
                    di = 2
            elif di == 2:
                if y == level:
                    di = 3
            elif di == 3:
                if x == level + 1:
                    di = 0
                    level += 1

            x += directions[di][0]
            y += directions[di][1]

        return res         
