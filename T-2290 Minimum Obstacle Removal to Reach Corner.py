'''
2290. Minimum Obstacle Removal to Reach Corner
https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

    0 represents an empty cell,
    1 represents an obstacle that may be removed.

You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from
the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

Example 1:

Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.

Example 2:

Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 105
    2 <= m * n <= 105
    grid[i][j] is either 0 or 1.
    grid[0][0] == grid[m - 1][n - 1] == 0
'''
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])
        heap = [(0, 0, 0)] # [(removed count, x, y,)]
        visited = {} # { (x, y) : removed count}
        visited[0, 0] = 0
        while heap:
            c, x, y = heappop(heap)
            if x == rowCount - 1 and y == colCount - 1:
                return c
            for i, j in (x, y+1), (x, y-1), (x+1, y), (x-1, y):
                if 0 <= i < rowCount and 0 <= j < colCount:
                    c2 = c if grid[i][j] == 0 else c + 1
                    if (i, j) not in visited or visited[i,j] > c2:
                        visited[i,j] = c2
                        heappush(heap, (c2, i, j))       
        return -1