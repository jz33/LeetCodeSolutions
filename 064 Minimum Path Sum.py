'''
64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 200
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])

        # Use input grid as DP buffer
        # The buffer can be 1D, since we only care about the last result
        for r in range(rowCount):
            for c in range(colCount):
                if r == 0 and c != 0:
                    grid[r][c] += grid[r][c-1]
                elif r != 0 and c == 0:
                    grid[r][c] += grid[r-1][c]
                elif r != 0 and c != 0:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])

        return grid[-1][-1]