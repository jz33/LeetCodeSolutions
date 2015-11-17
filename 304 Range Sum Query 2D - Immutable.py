import pprint
'''
Range Sum Query 2D - Immutable
https://leetcode.com/problems/range-sum-query-2d-immutable/
'''
pp = pprint.PrettyPrinter(indent=4)

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.mat = []
        ROW = len(matrix)
        if ROW == 0: return
        COL = len(matrix[0])
        if COL == 0: return
        mat = [[0 for i in xrange(COL+1)] for j in xrange(ROW+1)]
        for i in xrange(1,ROW+1):
            for j in xrange(1,COL+1):
                mat[i][j] = matrix[i-1][j-1] + mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
        self.mat = mat
        
        pp.pprint(mat)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        mat = self.mat
        col2 += 1
        row2 += 1
        return mat[row2][col2] + mat[row1][col1] - mat[row1][col2] - mat[row2][col1]

matrix = [
    [3,0,1,4,2],
    [5,6,3,2,1],
    [1,2,0,1,5],
    [4,1,0,1,7],
    [1,0,3,0,5]
    ]        
obj = NumMatrix(matrix)
print obj.sumRegion(2,1,4,3)
print obj.sumRegion(1,1,2,2)
print obj.sumRegion(1,2,2,4)     
        
