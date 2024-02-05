'''
694. Number of Distinct Islands
https://leetcode.com/problems/number-of-distinct-islands/

You are given an m x n binary matrix grid.
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if
one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.

Example 1:

Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

Example 2:

Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])
        visited = set()
        uniquePaths = set()

        def dfs(path: List[int], root: List[int]):
            rx, ry = root
            for ti, node in enumerate([(rx+1, ry), (rx-1, ry), (rx, ry+1), (rx, ry-1)]):
                tx, ty = node
                if tx >= 0 and tx < rowCount and ty >= 0 and ty < colCount and grid[tx][ty] == 1 and (tx, ty) not in visited:
                    visited.add((tx, ty))
                    path.append(ti)
                    dfs(path, [tx, ty])
            
            # Push the delimiter
            path.append(4)

        for r in range(rowCount):
            for c in range(colCount):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r,c))
                    # Record the path from [r ,c].
                    # '0' means down, '1' means up, '2' means right, '3' means left, '4' is delimiter
                    path = []
                    dfs(path, [r, c])
                    uniquePaths.add(''.join([str(p) for p in path]))
        return len(uniquePaths)