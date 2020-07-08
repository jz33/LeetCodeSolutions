'''
317. Shortest Distance from All Buildings
https://leetcode.com/problems/shortest-distance-from-all-buildings/

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.

Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
'''
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rowCount = len(grid)
        colCount = len(grid[0])
        
        # Find all buildings
        buildings = [] # [(x,y)]
        lands = {} # {(x, y) : [distances]}
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == 1:
                    buildings.append((i,j))
                elif grid[i][j] == 0:
                    lands[i,j] = []
                    
        if not lands or not buildings:
            return -1

        # Apply BFS from each buildings
        for bi, building in enumerate(buildings):  
            dist = 1
            stack = [building]
            while stack:
                newStack = []
                for x, y in stack:
                    for i, j in (x+1,y), (x,y+1), (x-1,y), (x,y-1):
                        # Be careful about how many buildings have already reached this land
                        if 0 <= i < rowCount and 0 <= j < colCount and grid[i][j] == 0 and len(lands[i,j]) == bi:
                            lands[i,j].append(dist)
                            newStack.append((i, j))

                stack = newStack
                dist += 1
            
        # Get minimum distance
        minDist = float('inf')
        for value in lands.values():
            # Make sure this land is reached by all buildings
            if len(value) == len(buildings):
                minDist = min(minDist, sum(value))
                
        return minDist if minDist != float('inf') else -1
