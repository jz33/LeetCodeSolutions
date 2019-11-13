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
from collections import deque
from collections import deque

INT_MAX = float('inf')

class Position:
    '''
    Represents a empty position on the grid.
    It records distances to all buildings,
    as well as last reached building index
    '''
    def __init__(self, buildingCount):
        self.distances = [INT_MAX] * buildingCount
        self.lastReachedBuildIndex = -1

    def isReachedBefore(self, buildingIndex: int) -> bool:
        '''
        If this position is reached by some builidings before.
        This position can either be reached by previous builidng, or current building
        '''
        return self.lastReachedBuildIndex == buildingIndex - 1 or self.lastReachedBuildIndex == buildingIndex

    def __repr__(self):
        return '{' + str(self.distances) + "," + str(self.lastReachedBuildIndex) + '}'
    
class Solution:
    def bfs(self, buildings, builidngMap):
        for bi, bp in enumerate(buildings):
            queue = deque()
            queue.append(bp)
            distance = 1
            while queue:
                for _ in range(len(queue)):
                    x,y = queue.popleft()
                    for i,j in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]:
                        if 0 <= i < self.rowCount and 0 <= j < self.colCount and self.grid[i][j] == 0:
                            position = builidngMap[i][j]
                            if position.isReachedBefore(bi) and distance < position.distances[bi]:
                                position.distances[bi] = distance
                                position.lastReachedBuildIndex = bi
                                queue.append((i,j))
                distance += 1
        
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        if rowCount == 0:
            return 0
        
        colCount = len(grid[0])
        if colCount == 0:
            return 0
        
        self.rowCount = rowCount
        self.colCount = colCount
        self.grid = grid
        
        # Find all buildings coordinates
        buildings = [(i,j) for i in range(rowCount) for j in range(colCount) if grid[i][j] == 1]
        buildingCount = len(buildings)
        
        # An equivalent matrix to record position information from each building
        buildingMap = [[Position(buildingCount) for _ in range(colCount)] for _ in range(rowCount)]

        # BFS for all buildings
        self.bfs(buildings, buildingMap)
            
        minDist = INT_MAX
        for i in range(rowCount):
            for j in range(colCount):
                if buildingMap[i][j].lastReachedBuildIndex == buildingCount - 1:
                    minDist = min(minDist, sum(buildingMap[i][j].distances))

        return minDist if minDist != INT_MAX else -1
