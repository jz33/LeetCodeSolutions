'''
1254. Number of Closed Islands
https://leetcode.com/problems/number-of-closed-islands/

Given a 2D grid consists of 0s (land) and 1s (water).
An island is a maximal 4-directionally connected group of 0s and
a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
'''
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])
        
        visited = [[False] * colCount for _ in range(rowCount)]
        
        def bfs(i: int, j: int) -> bool:
            visited[i][j] = True
            isClosed = True
            
            stack = [(i, j)]
            while stack:
                newStack = []
                for x, y in stack:
                    for a, b in (x, y+1), (x, y-1), (x+1, y), (x-1,y):
                        if 0 <= a < rowCount and 0 <= b < colCount:
                            if grid[a][b] == 0 and visited[a][b] is False:
                                visited[a][b] = True
                                newStack.append((a, b))
                        else:
                            isClosed = False
                stack = newStack
    
            return isClosed
        
        return sum(grid[i][j] == 0 and not visited[i][j] and bfs(i, j) for i in range(rowCount) for j in range(colCount))
