'''
407. Trapping Rain Water II
https://leetcode.com/problems/trapping-rain-water-ii/

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map,
compute the volume of water it is able to trap after raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

Constraints:

1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000
'''
from heapq import heappush, heappop, heapify

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        
        rowCount = len(heightMap)
        colCount = len(heightMap[0])
        seen = [[False] * colCount for _ in range(rowCount)]
        
        heap = [] # A min heap recording current position (x, y) and height, compared by height
        
        # Push in boundries to heap
        for i in range(rowCount):
            for j in [0, colCount-1]:
                seen[i][j] = True
                heap.append((heightMap[i][j], i, j))
                
        for j in range(1, colCount-1):
            for i in [0, rowCount-1]:
                seen[i][j] = True
                heap.append((heightMap[i][j], i, j))
                
        heapify(heap)
        
        # Push in inner nodes
        result = 0
        while heap:
            h, x, y = heappop(heap)
            for i, j in (x, y+1), (x, y-1), (x+1, y), (x-1, y):
                if 0 <= i < rowCount and 0 <= j < colCount and seen[i][j] is False:
                    seen[i][j] = True
                    
                    if h > heightMap[i][j]:
                        # The neighbor's height must be smaller than the smallest height (h) to hold a water
                        result += h - heightMap[i][j]
                        heappush(heap, (h, i, j))
                    else:
                        heappush(heap, (heightMap[i][j], i, j))

        return result
