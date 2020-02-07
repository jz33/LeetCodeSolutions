'''
741. Cherry Pickup
https://leetcode.com/problems/cherry-pickup/

In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.

Your task is to collect maximum number of cherries possible by following the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.

Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
 
Output: 5

Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
'''
from functools import lru_cache

class Solution:
    
    @lru_cache(None)
    def dfs(self, x0: int, y0: int, x1: int, y1: int) -> int:
        '''
        @return: return cherries picked. If cannot reach end, will return -1
        '''            
        cherries = -1
        N = len(self.grid)
        
        if x0 == N-1 and y0 == N-1:
            cherries = self.grid[x0][y0]      
        else:        
            for a, b, c ,d in [(x0, y0+1, x1, y1+1), (x0+1, y0, x1+1, y1), (x0, y0+1, x1+1, y1), (x0+1, y0, x1, y1+1)]:
                if a < N and b < N and c < N and d < N and self.grid[a][b] != -1 and self.grid[c][d] != -1:
                    cherries = max(cherries, self.dfs(a, b, c, d))

            if cherries >= 0:
                # Sub branch can reach end
                if x0 == x1 and y0 == y1:
                    cherries += self.grid[x0][y0]
                else:
                    cherries += self.grid[x0][y0] + self.grid[x1][y1]
 
        return cherries
                             
    def cherryPickup(self, grid: List[List[int]]) -> int:
        '''
        The picking process is from start to end and end to start,
        which equalavent to 2 person from start reaching end.
        '''        
        self.grid = grid      
        return max(self.dfs(0,0,0,0), 0)
