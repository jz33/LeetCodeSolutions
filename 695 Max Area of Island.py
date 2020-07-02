'''
695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array.
(If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
 
Given the above grid, return 6. Note the answer is not 11,
because the island must be connected 4-directionally.

Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rowCount = len(grid)
        colCount = len(grid[0])
        
        def bfs(i: int, j: int) -> int:
            area = 1
            grid[i][j] = 2 # Mark 2 as visited
            stack = [(i,j)]
            while stack:
                i,j = stack.pop()
                for x, y in (i,j+1), (i,j-1), (i+1,j),(i-1,j):
                    if 0 <= x < rowCount and 0 <= y < colCount and grid[x][y] == 1:
                        # Mark visited before push to avoid pushing duplicates into stack
                        grid[x][y] = 2
                        area += 1
                        stack.append((x,y))
            return area

        maxArea = 0
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, bfs(i,j))
        return maxArea
