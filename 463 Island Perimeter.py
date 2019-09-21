'''
463. Island Perimeter
https://leetcode.com/problems/island-perimeter/

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Input:
[[1,1,0],
 [1,1,1]]
 
Output: 10
'''
from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        if not rowCount:
            return 0
        colCount = len(grid[0])
        if not colCount:
            return 0
        
        IsIsland = 1
        IsInsideQueue = -1
        IsCounted = -2
        def count(x: int, y: int, added: int, dq: deque) -> int:
            if grid[x][y] == IsIsland:
                dq.append((x,y))
                grid[x][y] = IsInsideQueue
            elif grid[x][y] == IsCounted:
                added -= 2
            return added
                    
        perimeter = 0
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == IsIsland:
                    # BFS
                    dq = deque()
                    dq.append((i,j))
      
                    while dq:
                        x,y = dq.popleft()
                        grid[x][y] = IsCounted                                      
                        # Newly added perimeter count from x, y
                        # Can be negative!
                        added = 4
                        
                        if x+1 < rowCount:
                            added = count(x+1, y, added, dq)
                        if x > 0:
                            added = count(x-1, y, added, dq)
                        if y+1 < colCount:
                            added = count(x, y+1, added, dq)
                        if y > 0:
                            added = count(x, y-1, added, dq)
  
                        perimeter += added                            
        return perimeter
