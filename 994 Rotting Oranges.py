'''
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])
        
        # Gather all rotten oranges, fresh orange count
        freshCount = 0
        rottens = []
        for i in range(rowCount):
            for j in range(colCount):
                v = grid[i][j]
                if v == 1:
                    freshCount += 1
                elif v == 2:
                    rottens.append((i,j))
  
        # Apply BFS for all rotten oranges.
        # Notice not all oranges are going to be rotten
        steps = 0
        while rottens and freshCount:
            newRottens = []
            for x, y in rottens:
                for a, b in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if 0 <= a < rowCount and 0 <= b < colCount and grid[a][b] == 1:
                        grid[a][b] = 2
                        newRottens.append((a,b))

            freshCount -= len(newRottens)
            rottens = newRottens
            steps += 1
 
        return steps if freshCount == 0 else -1
