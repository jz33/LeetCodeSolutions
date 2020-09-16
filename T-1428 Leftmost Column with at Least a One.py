'''
1428. Leftmost Column with at Least a One
https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1.
For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it.
If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples.
You will not have access the binary matrix directly.

Example 1:

Input: mat = [[0,0],[1,1]]
Output: 0

Example 2:

Input: mat = [[0,0],[0,1]]
Output: 1

Example 3:

Input: mat = [[0,0],[0,0]]
Output: -1

Example 4:

Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1

Constraints:

rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.
'''
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, bm: 'BinaryMatrix') -> int:
        # Constants
        rowCount, colCount = bm.dimensions()
        
        # Result
        res = colCount
        
        # Column check cache
        top = 0
        
        # Binary search indexes
        left = 0
        right = colCount - 1
   
        while left <= right:
            mid = (left + right) // 2
            
            # Check column 'mid' from 'top'
            foundOne = True
            for i in range(top, rowCount):
                if bm.get(i, mid) == 1:
                    top = i
                    break
            else:
                foundOne = False
                    
            if foundOne:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return -1 if res == colCount else res
