'''
317. Shortest Distance from All Buildings
https://leetcode.com/problems/shortest-distance-from-all-buildings/

You are given an m x n grid grid of values 0, 1, or 2, where:

    each 0 marks an empty land that you can pass by freely,
    each 1 marks a building that you cannot pass through, and
    each 2 marks an obstacle that you cannot pass through.

You want to build a house on an empty land that reaches all buildings in the shortest total travel distance.
You can only move up, down, left, and right.

Return the shortest travel distance for such a house.
If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example 1:

Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.

Example 2:

Input: grid = [[1,0]]
Output: 1

Example 3:

Input: grid = [[1]]
Output: -1

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0, 1, or 2.
    There will be at least one building in the grid.
'''
class Solution:
    '''
    Real DoorDash interview question 20240207
    Time complexity: (N * M) ^ 2
    '''
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])
        
        # Find all buildings and lands
        buildings = [] # [(x,y)]
        lands = {} # {(x, y) : [distances to all buildings]}
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == 1:
                    buildings.append((i,j))
                elif grid[i][j] == 0:
                    lands[i,j] = []

        if not lands or not buildings:
            return -1

        # Apply BFS from each building, compute distances on each land
        for bi, building in enumerate(buildings):  
            dist = 1
            row = [building]
            while row:
                newRow = []
                for x, y in row:
                    for i, j in (x+1,y), (x,y+1), (x-1,y), (x,y-1):
                        # Only if lands[i, j == bi means in this BFS, this land has not yet been reached
                        if 0 <= i < rowCount and 0 <= j < colCount and grid[i][j] == 0 and len(lands[i,j]) == bi:
                            lands[i,j].append(dist)
                            newRow.append((i, j))

                row = newRow
                dist += 1
            
        # Get minimum distance
        minDist = float('inf')
        for distances in lands.values():
            # Make sure this land is reached by all buildings
            if len(distances) == len(buildings):
                minDist = min(minDist, sum(distances))
                
        return minDist if minDist != float('inf') else -1
