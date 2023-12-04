'''
1091. Shortest Path in Binary Matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected
(i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 100
    grid[i][j] is 0 or 1
'''
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        width = len(grid)
        seen = [[False] * width for _ in range(width)]
        seen[0][0] = True
        
        points = [(0,0)]
        steps = 0
        while points:
            newPoints = []
            for x, y in points:
                if x == width - 1 and y == width - 1:
                    return steps + 1 
                for d0, d1 in [(1,1),(0,1),(1,0),(1,-1),(0,-1),(-1,1),(-1,0),(-1,-1)]:
                    i, j = x + d0, y + d1
                    if 0 <= i < width and 0 <= j < width and grid[i][j] == 0 and not seen[i][j]:
                        seen[i][j] = True
                        newPoints.append((i,j))
            steps += 1
            points = newPoints
        return -1
