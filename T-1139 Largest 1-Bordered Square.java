/*
1139. Largest 1-Bordered Square
https://leetcode.com/problems/largest-1-bordered-square/

Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that
has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

Example 1:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9

Example 2:

Input: grid = [[1,1,0,0]]
Output: 1
 

Constraints:

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1
*/
class Solution {
    public int largest1BorderedSquare(int[][] grid) {
        int rowCount = grid.length;
        int colCount = grid[0].length;
        
        // Prefix matrix on row / column directions
        int[][] rowAccu = new int[rowCount][colCount];
        int[][] colAccu = new int[rowCount][colCount];
        
        // Build prefix matrices
        for (int i = 0; i < rowCount; ++i) {
            for (int j = 0; j < colCount; ++j) {
                if (grid[i][j] == 1) {
                    rowAccu[i][j] = (i > 0 ? rowAccu[i-1][j] + 1 : 1);
                    colAccu[i][j] = (j > 0 ? colAccu[i][j-1] + 1 : 1);
                }
            }
        }
        
        // Dynamic Programming
        int maxSize = 0;
        for (int i = 0; i < rowCount; ++i) {
            for (int j = 0; j < colCount; ++j) {
                if (grid[i][j] == 1) {
                    
                    // Check square bounds ends in (i,j)
                    int size = Math.min(rowAccu[i][j], colAccu[i][j]);
                    
                    // Check the other 2 bounds. Notice the while loop is
                    // to find any fit square ends in (i,j)
                    while (size > maxSize) {
                        // Verify the other 2 bounds
                        if (rowAccu[i][j-size+1] >= size && colAccu[i-size+1][j] >= size) {
                            maxSize = size;
                        }
                        size -= 1;
                    }
                }
            }
        }
        
        return maxSize * maxSize;
    }
}
