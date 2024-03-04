'''
1293. Shortest Path in a Grid with Obstacles Elimination
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0)
to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles.
If it is not possible to find such walk return -1.

Example 1:

Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example 2:

Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 40
    1 <= k <= m * n
    grid[i][j] is either 0 or 1.
    grid[0][0] == grid[m - 1][n - 1] == 0
'''
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])
        
        queue = deque([(0, 0, k)]) # [(x, y, available elimination count)]
        visited = {(0, 0, k)}
        steps = 0
        while queue:
            for _ in range(len(queue)):
                x, y, r = queue.popleft()
                if x == rowCount - 1 and y == colCount - 1:
                    return steps
                
                for i, j in (x, y+1), (x, y-1), (x+1, y), (x-1, y):
                    if 0 <= i < rowCount and 0 <= j < colCount:
                        if grid[i][j] == 0:
                            newNode = (i, j, r)
                            if newNode not in visited:
                                visited.add(newNode)
                                queue.append(newNode)
                        elif r > 0:
                            newNode = (i, j, r-1)
                            if newNode not in visited:
                                visited.add(newNode)
                                queue.append(newNode)             
            steps += 1
        return -1