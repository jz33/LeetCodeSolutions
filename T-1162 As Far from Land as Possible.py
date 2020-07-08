'''
1162. As Far from Land as Possible
https://leetcode.com/problems/as-far-from-land-as-possible/

Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land,
find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

Example 1:

Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:

Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1
'''
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])
        
        # Get all lands
        lands = []
        hasWater = False
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == 1:
                    lands.append((i,j))
                else:
                    hasWater = True
        
        if not hasWater or not lands:
            return -1

        # Group BFS for all lands
        seen = [[False] * colCount for _ in range(rowCount)]
        dist = -1 # Be careful of iteration count!
        while lands:
            newLands = []
            for i,j in lands:
                for x, y in (i, j+1), (i, j-1), (i+1, j), (i-1, j):
                    if 0 <= x < rowCount and 0 <= y < colCount and grid[x][y] == 0 and seen[x][y] is False:
                        seen[x][y] = True
                        newLands.append((x, y))
            lands = newLands
            dist += 1
        return dist
