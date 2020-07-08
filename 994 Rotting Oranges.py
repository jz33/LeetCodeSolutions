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
INF = float('inf')

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rowCount = len(grid)
        colCount = len(grid[0])
        
        # Gather all rotten oranges, fresh orange count
        freshCount = 0
        rottens = [] # Use simpler stakc
        for i in range(rowCount):
            for j in range(colCount):
                v = grid[i][j]
                if v == 1:
                    freshCount += 1
                elif v == 2:
                    rottens.append((i,j))
                
        # Apply BFS for all rotten oranges. This is faster than apply 1 by 1.
        steps = 0
        while rottens and freshCount:
            newRottens = []
            for x, y in rottens:
                for a, b in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if 0 <= a < rowCount and 0 <= b < colCount and grid[a][b] == 1:
                        freshCount -= 1
                        grid[a][b] = 2
                        newRottens.append((a,b))
            rottens = newRottens
            steps += 1
 
        return steps if freshCount == 0 else -1
