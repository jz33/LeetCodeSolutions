'''
1905. Count Sub Islands
https://leetcode.com/problems/count-sub-islands/

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water)
and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical).
Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Example 1:

Input:
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

Example 2:

Input:
grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.

Constraints:
    m == grid1.length == grid2.length
    n == grid1[i].length == grid2[i].length
    1 <= m, n <= 500
    grid1[i][j] and grid2[i][j] are either 0 or 1.
'''
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rowCount = len(grid2)
        colCount = len(grid2[0])
        subIslands = 0
        VISITED = -1 # mark visited on grid2

        def dfs(r: int, c: int) -> bool:
            isSubIsland = grid1[r][c] == 1
            for x, y in (r+1,c),(r-1,c),(r,c+1),(r,c-1):
                if 0 <= x < rowCount and 0 <= y < colCount and grid2[x][y] == 1:
                    grid2[x][y] = VISITED
                    if not dfs(x, y):
                        isSubIsland = False
            return isSubIsland

        for r in range(rowCount):
            for c in range(colCount):
                if grid2[r][c] == 1:
                    grid2[r][c] = VISITED
                    if dfs(r, c):
                        subIslands += 1
        return subIslands