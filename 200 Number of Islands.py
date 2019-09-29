'''
Number of Islands
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowCount = len(grid)
        if rowCount == 0:
            return 0
        
        colCount = len(grid[0])
        if colCount == 0:
            return 0
        
        LAND = '1'
        INQUEUE = '2'
        POPED = '3'
        
        def mark(i: int, j: int):
            stack = [(i,j)]
            while len(stack) > 0:
                x, y = stack.pop()
                grid[x][y] = POPED
                if x+1 < rowCount and grid[x+1][y] == LAND:
                    stack.append((x+1,y))
                    grid[x+1][y] = INQUEUE # Mark here to avoid duplicates in queue!
                if x-1 > -1 and grid[x-1][y] == LAND:
                    stack.append((x-1,y))
                    grid[x-1][y] = INQUEUE
                if y+1 < colCount and grid[x][y+1] == LAND:
                    stack.append((x,y+1))
                    grid[x][y+1] = INQUEUE
                if y-1 > -1 and grid[x][y-1] == LAND:
                    stack.append((x,y-1))
                    grid[x][y-1] = INQUEUE
                 
        res = 0
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == LAND:
                    res += 1
                    mark(i,j)
        
        return res
