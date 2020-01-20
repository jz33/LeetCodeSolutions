'''
361. Bomb Enemy

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
'''
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rowCount = len(grid)
        colCount = len(grid[0])       
        
        # dp[i][j] is array of 4 means bomb counts left, up, right, down of (i,j)
        dp = [[[0] * 4 for _ in range(colCount)] for _ in range(rowCount)]
        
        # Update left and up bomb counts
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] != 'W':
                    if j > 0:
                        dp[i][j][0] = dp[i][j-1][0] + int(grid[i][j-1] == 'E')
                    if i > 0:
                        dp[i][j][1] = dp[i-1][j][1] + int(grid[i-1][j] == 'E')
                        
        # Update right and down bomb counts
        for i in range(rowCount-1,-1,-1):
            for j in range(colCount-1,-1,-1):
                if grid[i][j] != 'W':
                    if j < colCount - 1:
                        dp[i][j][2] = dp[i][j+1][2] + int(grid[i][j+1] == 'E')
                    if i < rowCount - 1:
                        dp[i][j][3] = dp[i+1][j][3] + int(grid[i+1][j] == 'E')
                        
        # Get max bomb
        bombs = [sum(dp[i][j]) for i in range(rowCount) for j in range(colCount) if grid[i][j] == '0']
        return max(bombs) if len(bombs) > 0 else 0
