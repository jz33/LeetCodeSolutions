'''
200. Number of Islands
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
    def bfs(self, grid, visited, start):
        queue = collections.deque([start])
        visited[start[0]][start[1]] = True
        while queue:
            i,j = queue.popleft()
            for x,y in (i,j+1),(i+1,j),(i,j-1),(i-1,j):
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1' and visited[x][y] is False:
                    queue.append((x,y))
                    visited[x][y] = True
                
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rowCount = len(grid)
        colCount = len(grid[0])
        visited = [[False] * colCount for _ in range(rowCount)]
        island = 0
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == '1' and visited[i][j] is False:
                    self.bfs(grid, visited, (i,j))
                    island += 1
        return island

    
class Solution:
    '''
    DFS
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rowCount = len(grid)
        colCount = len(grid[0])
        visited = [[False] * colCount for _ in range(rowCount)]
        
        def dfs(i, j):
            nonlocal visited
            if 0 <= i < rowCount and 0 <= j < colCount and grid[i][j] == '1' and visited[i][j] == False:
                visited[i][j] = True                
                for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                    dfs(x, y)
                
        # Set of direction paths
        islandCount = 0
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == '1' and visited[i][j] == False:
                    islandCount += 1
                    dfs(i, j)

        return islandCount
