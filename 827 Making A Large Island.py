'''
827. Making A Large Island
https://leetcode.com/problems/making-a-large-island/

You are given an n x n binary matrix grid.
You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 500
    grid[i][j] is either 0 or 1.
'''
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])

        islands = {} # {island index : total area}
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == 1:
                    # Mark grid to the island's index and count area.
                    # As the grid has 0 or 1, the island start should start from 2
                    area = 1
                    islandIndex = len(islands.keys()) + 2
                    grid[i][j] = islandIndex
                    row = [(i,j)]
                    while row:
                        newRow = []
                        for x, y in row:
                            for a,b in (x,y+1), (x,y-1), (x+1,y), (x-1,y):
                                if 0 <= a < rowCount and 0 <= b < colCount and grid[a][b] == 1:
                                    grid[a][b] = islandIndex
                                    area += 1
                                    newRow.append((a,b))
                        row = newRow
                    islands[islandIndex] = area

        maxArea = max(islands.values()) if islands else 0
        for x in range(rowCount):
            for y in range(colCount):
                if grid[x][y] == 0:
                    # For each empty slot, check if it connects islands,
                    # then calculate total area
                    neighborIslands = set()
                    for a,b in (x,y+1), (x,y-1), (x+1,y), (x-1,y):
                        if 0 <= a < rowCount and 0 <= b < colCount and grid[a][b] > 1:
                            neighborIslands.add(grid[a][b])
                    maxArea = max(maxArea, sum(islands.get(islandIndex, 0) for islandIndex in neighborIslands) + 1)
        return maxArea
