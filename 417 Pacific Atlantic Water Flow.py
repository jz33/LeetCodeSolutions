'''
417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''
class Solution:
    def bfs(self, matrix, rowCount, colCount, start, visited):
        x,y = start
        if visited[x][y] is True:
            return
        visited[x][y] = True
        
        queue = collections.deque([start])
        while queue:
            x,y = queue.popleft()
            for inc in (0,1),(1,0),(0,-1),(-1,0):
                i,j = x + inc[0], y + inc[1]
                if 0 <= i < rowCount and 0 <= j < colCount and visited[i][j] is False and matrix[i][j] >= matrix[x][y]:
                    visited[i][j] = True
                    queue.append((i,j))
        
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        
        rowCount = len(matrix)
        colCount = len(matrix[0])
        
        pacificVisited = [[False] * colCount for _ in range(rowCount)]
        for i in range(rowCount):
            self.bfs(matrix, rowCount, colCount, (i,0), pacificVisited)
        for i in range(colCount):
            self.bfs(matrix, rowCount, colCount, (0,i), pacificVisited)
                    
        atlanticVisited = [[False] * colCount for _ in range(rowCount)]
        for i in range(rowCount):
            self.bfs(matrix, rowCount, colCount, (i,colCount-1), atlanticVisited)
        for i in range(colCount):
            self.bfs(matrix, rowCount, colCount, (rowCount-1,i), atlanticVisited)
            
        return [[i,j] for i in range(rowCount) for j in range(colCount) if pacificVisited[i][j] is True and atlanticVisited[i][j] is True]
