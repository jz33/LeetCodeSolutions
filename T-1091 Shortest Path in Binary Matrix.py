'''
1091. Shortest Path in Binary Matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.
If such a path does not exist, return -1.
'''
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        rowCount = len(grid)
        colCount = len(grid[0])
        if rowCount == 1 and colCount == 1:
            return 1

        seen = [[False] * colCount for _ in range(rowCount)]
        seen[0][0] = True
        
        points = [(0,0)]
        steps = 1
        while points:
            newPoints = []
            for x, y in points:   
                for d0, d1 in [(1,1),(0,1),(1,0),(1,-1),(0,-1),(-1,1),(-1,0),(-1,-1)]:
                    i, j = x + d0, y + d1
                    if i == rowCount - 1 and j == colCount - 1:
                        return steps + 1
                    if 0 <= i < rowCount and 0 <= j < colCount and grid[i][j] == 0 and not seen[i][j]:
                        seen[i][j] = True
                        newPoints.append((i,j))
            steps += 1
            points = newPoints
        return -1
