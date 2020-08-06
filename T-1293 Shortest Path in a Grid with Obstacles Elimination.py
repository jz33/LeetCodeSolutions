'''
1293. Shortest Path in a Grid with Obstacles Elimination
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle).
In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to
the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles.
If it is not possible to find such walk return -1.

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6.
Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 

Example 2:

Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
'''
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])
        
        stack = [(0, 0, k)] # [(x, y, available elimination count)]
        visited = {(0, 0, k)}
        steps = 0
        while stack:
            newStack = []
            for x, y, r in stack:
                if x == rowCount - 1 and y == colCount - 1:
                    return steps
                
                for i, j in (x, y+1), (x, y-1), (x+1, y), (x-1, y):
                    if 0 <= i < rowCount and 0 <= j < colCount:
                        if grid[i][j] == 0:
                            node = (i, j, r)
                            if node not in visited:
                                visited.add(node)
                                newStack.append(node)
                                
                        elif r > 0:
                            node = (i, j, r-1)
                            if node not in visited:
                                visited.add(node)
                                newStack.append(node)
                                
            stack = newStack
            steps += 1
            
        return -1
