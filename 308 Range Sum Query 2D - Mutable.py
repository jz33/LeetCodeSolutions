'''
308. Range Sum Query 2D - Mutable
https://leetcode.com/problems/range-sum-query-2d-mutable/

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by
its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3),
which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
'''
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.isfucked = not matrix or not matrix[0]
        if self.isfucked:
            return
        
        rowCount = len(matrix)
        colCount = len(matrix[0])
        
        self.nums = [[0] * colCount for _ in range(rowCount)]
        self.bits = [[0] * (colCount+1) for _ in range(rowCount+1)]
        
        for i in range(rowCount):
            for j in range(colCount):
                self.update(i,j,matrix[i][j])
                
    def update(self, row: int, col: int, val: int) -> None:
        if self.isfucked:
            return
        
        diff = val - self.nums[row][col]
        if diff != 0:
            self.nums[row][col] = val
            
            rowCount = len(self.nums)
            colCount = len(self.nums[0])
        
            i = row + 1
            while i <= rowCount:
                j = col + 1
                while j <= colCount:
                    self.bits[i][j] += diff
                    j += (j & -j)
                i += (i & -i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.isfucked:
            return 0
        
        return self.getSum(row2+1, col2+1) - self.getSum(row1, col2+1) - self.getSum(row2+1, col1) + self.getSum(row1, col1)
    
    def getSum(self, row: int, col: int) -> int:
        total = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                total += self.bits[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return total
