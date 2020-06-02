'''
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''
from collections import deque

INF = float('inf')

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rowCount = len(grid)
        colCount = len(grid[0])
        
        # Records shortest distance from a good orange to a rotten orange
        mat = [[INF] * colCount for _ in range(rowCount)]

        for i in range(rowCount):
            for j in range(colCount):
                # BFS from rotten orange
                if grid[i][j] == 2:
                    queue = deque([(i,j)])
                    dist = 1
                    while queue:
                        for _ in range(len(queue)):
                            x, y = queue.popleft()
                            for a, b in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                                if 0 <= a < rowCount and 0 <= b < colCount and grid[a][b] == 1 and dist < mat[a][b]:
                                    mat[a][b] = dist
                                    queue.append((a,b))
                        dist += 1
        
        maxD = 0
        for i in range(rowCount):
            for j in range(colCount): 
                if grid[i][j] == 1:
                    if mat[i][j] == INF:
                        return -1
                    maxD = max(maxD, mat[i][j])
 
        return maxD
