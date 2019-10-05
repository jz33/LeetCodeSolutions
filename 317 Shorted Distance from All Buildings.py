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
from typing import Tuple
from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        if rowCount == 0:
            return 0
        
        colCount = len(grid[0])
        if colCount == 0:
            return 0
        
        def extend(x: int, y: int, bi: int, queue, d):
            if x < rowCount and x > -1 and y < colCount and y > -1 and grid[x][y] == 0:
                old_d = buildingMap[x][y][bi]
                if old_d is None or old_d > d:
                    buildingMap[x][y][bi] = d
                    queue.append((x, y, d))

        def broadcast(bp: Tuple[int, int], bi: int):
            '''
            Set all distances for a building
            @bp: building position
            @bi: building index
            '''
            queue = deque() # [(building position x, y, distance)]
            queue.append((bp[0], bp[1], 0))

            while queue:
                x, y, d = queue.popleft()
                extend(x+1, y, bi, queue, d+1)
                extend(x, y+1, bi, queue, d+1)
                extend(x-1, y, bi, queue, d+1)
                extend(x, y-1, bi, queue, d+1)

        buildings = []
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == 1:
                    buildings.append((i,j))

        # A 3-D matrix to record shortest distances to each building.
        # The buildingMap[i][j][k] means the shortest distance to building k from (i, j).
        # If (i, j) is obstacle or building itself, the value is always None
        buildingMap = [[[None] * len(buildings) for _ in range(colCount)] for _ in range(rowCount)]
        for i, b in enumerate(buildings):
            broadcast(b, i)

        # Get minimum
        MaxDist = rowCount * colCount * len(buildings)
        def sumDist(x: int, y: int) -> int:
            '''
            Sum all distances on buildingMap[x][y]
            If any is None, then this point cannot reach all buildins
            '''
            s = 0
            for d in buildingMap[x][y]:
                if d is None:
                    return MaxDist
                s += d
            return s

        minDist = MaxDist
        for i in range(rowCount):
            for j in range(colCount):
                minDist = min(minDist, sumDist(i, j))

        return minDist if minDist != MaxDist else -1
