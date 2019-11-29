'''
498. Diagonal Traverse
https://leetcode.com/problems/diagonal-traverse/

Given a matrix of M x N elements (M rows, N columns),
return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]
'''
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        Try write in a concise way
        '''
        rowCount = len(matrix)
        if not rowCount:
            return []
        
        colCount = len(matrix[0])
        if not colCount:
            return []
              
        res = [None] * (rowCount * colCount)
        x, y = 0, 0
        for i in range(len(res)):
            res[i] = matrix[x][y]
            if (x + y) & 1 == 0:
                # Go upper right
                if y + 1 == colCount:
                    x += 1
                elif x == 0:
                    y += 1
                else:
                    x -= 1
                    y += 1
            else:
                # Go lower left
                if x + 1 == rowCount:
                    y += 1
                elif y == 0:
                    x += 1
                else:
                    x += 1
                    y -= 1
        return res     
