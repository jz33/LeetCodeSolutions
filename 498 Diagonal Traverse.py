'''
498. Diagonal Traverse
https://leetcode.com/problems/diagonal-traverse/

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 104
    1 <= m * n <= 104
    -105 <= mat[i][j] <= 105
'''
class Solution:
    '''
    Direct go through matrix diagonally
    Cannot avoid empty cells (rows having different length)
    '''
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
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

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list) # { diagonalIndex : [values] }
        for ri in range(len(nums)):
            for ci in range(len(nums[ri])):
                diagonalIndex = ri + ci
                diagonals[diagonalIndex].append(nums[ri][ci])
        
        result = []
        for d in range(len(diagonals.keys())):
            if d & 1 == 0:
                result += reversed(diagonals[d])
            else:
                result += diagonals[d]
        return result