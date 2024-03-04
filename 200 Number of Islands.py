'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'
'''
class Solution:
    '''
    BFS
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rowCount = len(grid)
        colCount = len(grid[0])
        visited = [[False] * colCount for _ in range(rowCount)]
        island = 0

        for r in range(rowCount):
            for c in range(colCount):
                if grid[r][c] == '1' and visited[r][c] is False:
                    queue = deque([(r, c)])
                    visited[r][c] = True
                    while queue:
                        i,j = queue.popleft()
                        for x, y in (i,j+1),(i+1,j),(i,j-1),(i-1,j):
                            if 0 <= x < rowCount and 0 <= y < colCount and grid[x][y] == '1' and visited[x][y] is False:
                                visited[x][y] = True
                                queue.append((x, y))
                    island += 1
        return island
    
class Solution2:
    '''
    DFS
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rowCount = len(grid)
        colCount = len(grid[0])
        visited = [[False] * colCount for _ in range(rowCount)]

        def dfs(i: int, j: int):
            for x, y in (i,j+1),(i+1,j),(i,j-1),(i-1,j):
                if 0 <= x < rowCount and 0 <= y < colCount and grid[x][y] == '1' and visited[x][y] is False:
                    visited[x][y] = True
                    dfs(x, y)

        island = 0
        for r in range(rowCount):
            for c in range(colCount):
                if grid[r][c] == '1' and visited[r][c] is False:
                    visited[r][c] = True
                    dfs(r, c)
                    island += 1
        return island