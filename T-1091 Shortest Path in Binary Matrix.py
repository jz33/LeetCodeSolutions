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
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        if rowCount == 0:
            return -1

        colCount = len(grid[0])
        if colCount == 0:
            return -1

        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        # Record shortest paths
        MAX_VALUE = (rowCount+1)*(colCount+1)
        paths = [[MAX_VALUE for _ in range(colCount)] for _ in range(rowCount)]

        queue = deque()
        queue.append((0,0))
        paths[0][0] = 1

        while queue:
            x,y = queue.popleft()
            p = paths[x][y]
            for d0, d1 in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
                i, j = x + d0, y + d1
                if -1 < i < rowCount and -1 < j < colCount and grid[i][j] != 1 and p+1 < paths[i][j]:
                    queue.append((i,j))
                    paths[i][j] = p+1

        return paths[-1][-1] if paths[-1][-1] != MAX_VALUE else -1
