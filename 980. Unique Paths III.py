'''
980. Unique Paths III
https://leetcode.com/problems/unique-paths-iii/

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square,
that walk over every non-obstacle square exactly once.

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
'''
from typing import Tuple

class Solution:
    def getInfo(self, grid: List[List[int]]):
        start = None
        end = None
        emptyCount = 0
        for i,row in enumerate(grid):
            for j,e in enumerate(row):
                if e == 1:
                    start = (i,j)
                elif e == 2:
                    end = (i,j)
                elif e == 0:
                    emptyCount += 1
        return start, end, emptyCount
              
    def backtrack(self, curr: Tuple[int, int], visitedCount: int, visited: List[List[bool]]):
        if curr == self.end:
            if visitedCount == self.emptyCount + 1: # +1 because end is also visited
                self.solutionCount += 1
        else:
            for inc in [[0,1],[1,0],[0,-1],[-1,0]]:
                i,j = curr[0]+inc[0], curr[1]+inc[1]
                if 0 <= i < self.rowCount and 0 <= j < self.colCount and visited[i][j] is False:
                    if self.grid[i][j] == 0 or self.grid[i][j] == 2:
                        visited[i][j] = True
                        self.backtrack((i,j), visitedCount+1, visited)                     
                        visited[i][j] = False
                        
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        start, self.end, self.emptyCount = self.getInfo(grid)
        
        self.rowCount = len(grid)
        self.colCount = len(grid[0])
        visited = [[False] * self.colCount for _ in range(self.rowCount)]
        
        self.grid = grid
        self.solutionCount = 0
        
        self.backtrack(start, 0, visited)

        return self.solutionCount
