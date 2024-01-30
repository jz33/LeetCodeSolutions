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
        colCount = len(matrix[0])
     
        result = [None] * (rowCount * colCount)
        r, c = 0, 0
        for i in range(len(result)):
            result[i] = matrix[r][c]
            if (r + c) & 1 == 0:
                # Go upper right
                if c + 1 == colCount:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                # Go lower left
                if r + 1 == rowCount:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
        return result     

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