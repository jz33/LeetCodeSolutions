/*
64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
*/
class Solution {
    public int minPathSum(int[][] grid) {
        int rowCount = grid.length;
        if (rowCount == 0) {
            return 0;
        }
        int colCount = grid[0].length;
        if (colCount == 0) {
            return 0;
        }
        
        // Use input grid as DP buffer
        // The buffer can be 1D, since we only care about the last result
        for (int i = 0; i < rowCount; i++) {
            for (int j = 0; j < colCount; j++) {
                if (i == 0 && j != 0) {
                    grid[i][j] += grid[i][j-1];
                }
                else if (i != 0 && j == 0) {
                    grid[i][j] += grid[i-1][j];
                }
                else if (i != 0 && j != 0) {
                    grid[i][j] += Math.min(grid[i][j-1], grid[i-1][j]);
                }
            }
        }
        return grid[rowCount-1][colCount-1];
    }
}
