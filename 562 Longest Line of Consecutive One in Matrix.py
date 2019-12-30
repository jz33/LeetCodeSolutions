'''
562. Longest Line of Consecutive One in Matrix
https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

Given a 01 matrix M, find the longest line of consecutive one in the matrix.
The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:

Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3

Hint: The number of elements in the given matrix will not exceed 10,000.
'''
class Solution:
    def inBound(self, x: int, y: int) -> bool:
        return 0 <= x < self.rowCount and 0 <= y < self.colCount
    
    def getDirections(self, x: int, y: int) -> List[List[int]]:
        '''
        To minimize duplicate computing, we only want iteration though
        Right, Down, Right Down, Left Down directions
        '''
        directions = []
        for dx, dy in [[0,1],[1,0],[1,1],[1,-1]]:
            # Try go back 1 step, if out of bound, this is the staring point.
            # Or back point is in bound but value is 0, this is also the starting point
            if not self.inBound(x-dx, y-dy) or self.mat[x-dx][y-dy] == 0:
                directions.append([dx,dy])
        return directions
            
    def longestLine(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        if not M[0]:
            return 0
        
        self.mat = M
        self.rowCount = len(M)
        self.colCount = len(M[0])
        maxLen = 0
        for i in range(self.rowCount):
            for j in range(self.colCount):
                if M[i][j] == 1:
                    maxLen = max(maxLen, 1)
                    for dx, dy in self.getDirections(i,j):
                        x,y = i,j
                        localLen = 1
                        while self.inBound(x+dx,y+dy) and M[x+dx][y+dy] == 1:
                            x,y = x+dx,y+dy
                            localLen += 1
                        maxLen = max(maxLen, localLen)
        return maxLen
