'''
1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbours
of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighboors if they share one edge.

Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

Binary matrix is a matrix with all cells equal to 0 or 1 only.

Zero matrix is a matrix with all cells equal to 0.

Example 1:

Input: mat = [[0,0],[0,1]]
Output: 3
Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.

Example 2:

Input: mat = [[0]]
Output: 0
Explanation: Given matrix is a zero matrix. We don't need to change it.

Example 3:

Input: mat = [[1,1,1],[1,0,1],[0,0,0]]
Output: 6

Example 4:

Input: mat = [[1,0,0],[1,0,0]]
Output: -1
Explanation: Given matrix can't be a zero matrix
 
Constraints:

m == mat.length
n == mat[0].length
1 <= m <= 3
1 <= n <= 3
mat[i][j] is 0 or 1.
'''
from heapq import heappush, heappop

class Solution:
    def bitmap(self, mat: List[List[int]]) -> int:
        rowCount = len(mat)
        colCount = len(mat[0])
        b = 0
        for i in range(self.rowCount):
            for j in range(self.colCount):
                if mat[i][j] == 1:
                    b |= (1 << (i * rowCount + j))
        return b

    def flip(self, mat: List[List[int]], x: int, y: int) -> List[List[int]]:
        newMat = copy.deepcopy(mat)
        newMat[x][y] = 1 - newMat[x][y]
        for i,j in (x,y+1), (x+1,y), (x,y-1),(x-1,y):
            if 0 <= i < self.rowCount and 0 <= j < self.colCount:
                newMat[i][j] = 1 - newMat[i][j]
        return newMat

    def minFlips(self, mat: List[List[int]]) -> int:
        '''
        Dijkstra with memorization
        '''     
        self.rowCount = len(mat)
        self.colCount = len(mat[0])

        computed = set() # {bitmap of binary matrix}
        heap = [(0, mat)] # [(steps, matrix)]
        while heap:
            steps, node = heappop(heap)
            bitmap = self.bitmap(node)
            if bitmap in computed:
                continue

            if bitmap == 0:
                return steps

            computed.add(bitmap)

            for i in range(self.rowCount):
                for j in range(self.colCount):
                    newNode = self.flip(node, i, j)
                    heappush(heap, (steps+1, newNode))

        return -1
